#!/usr/bin/env python3
"""
Orchestra Launch Video Generator
Generates video clips using Google Veo 3.1 API based on prepared prompts.
Handles rate limiting and video extension for connected scenes.
"""

import os
import time
import json
from pathlib import Path
from typing import Optional, Dict, Any
from datetime import datetime
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from .env file
load_dotenv()

# Configuration
API_KEY = os.getenv("GOOGLE_API_KEY")
OUTPUT_DIR = Path(__file__).parent.parent / "output"
METADATA_FILE = OUTPUT_DIR / "generation_metadata.json"

# Rate limiting
WAIT_BETWEEN_REQUESTS = 60  # seconds between requests to avoid rate limits

class VeoVideoGenerator:
    """Generator for Orchestra launch video clips using Veo 3.1"""

    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set")

        self.api_key = api_key
        self.client = genai.Client(api_key=api_key)
        self.metadata = self._load_metadata()
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    def _load_metadata(self) -> Dict[str, Any]:
        """Load previous generation metadata if exists"""
        if METADATA_FILE.exists():
            with open(METADATA_FILE, 'r') as f:
                return json.load(f)
        return {"clips": {}, "generation_history": []}

    def _save_metadata(self):
        """Save generation metadata"""
        with open(METADATA_FILE, 'w') as f:
            json.dump(self.metadata, f, indent=2)

    def generate_clip(
        self,
        clip_id: str,
        prompt: str,
        duration: int = 8,
        resolution: str = "1080p",
        aspect_ratio: str = "16:9",
        extend_from_clip: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate a video clip using Veo 3.1 API

        Args:
            clip_id: Identifier for the clip (e.g., "clip_1_galileo")
            prompt: Text prompt for video generation
            duration: Duration in seconds (max 8)
            resolution: "720p" or "1080p"
            aspect_ratio: "16:9", "9:16", etc.
            extend_from_clip: Optional clip_id to extend from

        Returns:
            Dict with generation results including video file path
        """
        print(f"\n{'='*60}")
        print(f"Generating: {clip_id}")
        print(f"Duration: {duration}s | Resolution: {resolution}")
        print(f"Extend from: {extend_from_clip or 'None (independent)'}")
        print(f"{'='*60}\n")

        # Check if already generated
        if clip_id in self.metadata["clips"]:
            print(f"⚠️  Clip {clip_id} already generated. Skipping.")
            return self.metadata["clips"][clip_id]

        try:
            print(f"🎬 Sending request to Veo 3.1 API...")

            # Prepare generation config
            config = types.GenerateVideosConfig(
                duration_seconds=duration,
                resolution=resolution,
                aspect_ratio=aspect_ratio,
                number_of_videos=1
            )

            # Generate video with or without extension
            if extend_from_clip:
                if extend_from_clip not in self.metadata["clips"]:
                    raise ValueError(f"Cannot extend from {extend_from_clip}: not yet generated")

                # Get the previous video file for extension
                prev_video_path = self.metadata["clips"][extend_from_clip].get("video_path")
                if not prev_video_path or not Path(prev_video_path).exists():
                    raise ValueError(f"Cannot extend from {extend_from_clip}: video file not found")

                print(f"📎 Extending from previous clip: {extend_from_clip}")

                # Upload the previous video for extension
                with open(prev_video_path, 'rb') as f:
                    prev_file = self.client.files.upload(file=f)

                # Generate with video extension
                operation = self.client.models.generate_videos(
                    model="veo-3.1-generate-preview",
                    prompt=prompt,
                    config=config,
                    video=prev_file
                )
            else:
                # Generate independent clip
                operation = self.client.models.generate_videos(
                    model="veo-3.1-generate-preview",
                    prompt=prompt,
                    config=config
                )

            print(f"⏳ Waiting for video generation to complete...")
            print(f"   (This can take 10 seconds to 6 minutes)")

            # Poll the operation status until the video is ready
            poll_count = 0
            while not operation.done:
                time.sleep(10)
                poll_count += 1
                print(f"   Still generating... ({poll_count * 10}s elapsed)")
                operation = self.client.operations.get(operation)

            # Download the generated video
            generated_video = operation.response.generated_videos[0]
            video_filename = f"{clip_id}.mp4"
            video_path = OUTPUT_DIR / video_filename

            print(f"⬇️  Downloading generated video...")
            self.client.files.download(file=generated_video.video)
            generated_video.video.save(str(video_path))

            # Store result
            clip_data = {
                "clip_id": clip_id,
                "prompt": prompt,
                "duration": duration,
                "resolution": resolution,
                "aspect_ratio": aspect_ratio,
                "extend_from": extend_from_clip,
                "video_path": str(video_path),
                "video_filename": video_filename,
                "generated_at": datetime.now().isoformat(),
                "generation_time_seconds": poll_count * 10
            }

            self.metadata["clips"][clip_id] = clip_data
            self.metadata["generation_history"].append({
                "clip_id": clip_id,
                "timestamp": datetime.now().isoformat(),
                "status": "success"
            })
            self._save_metadata()

            print(f"✅ Successfully generated {clip_id}")
            print(f"📹 Video saved to: {video_path}")

            return clip_data

        except Exception as e:
            error_msg = f"❌ Error generating {clip_id}: {str(e)}"
            print(error_msg)

            self.metadata["generation_history"].append({
                "clip_id": clip_id,
                "timestamp": datetime.now().isoformat(),
                "status": "failed",
                "error": str(e)
            })
            self._save_metadata()

            raise

    def generate_sequence(self, clips: list[Dict[str, Any]], wait_between: int = WAIT_BETWEEN_REQUESTS):
        """
        Generate a sequence of clips with rate limiting

        Args:
            clips: List of clip configurations
            wait_between: Seconds to wait between requests
        """
        total_clips = len(clips)

        print(f"\n🎥 Starting generation sequence: {total_clips} clips")
        print(f"⏱️  Wait time between requests: {wait_between}s")

        for i, clip_config in enumerate(clips, 1):
            print(f"\n📍 Progress: {i}/{total_clips}")

            try:
                self.generate_clip(**clip_config)

                # Wait before next request (except for last clip)
                if i < total_clips:
                    print(f"\n⏳ Waiting {wait_between}s before next request...")
                    time.sleep(wait_between)

            except Exception as e:
                print(f"\n⚠️  Failed to generate clip {i}/{total_clips}")
                print(f"Error: {str(e)}")

                # Ask user whether to continue
                response = input("\nContinue with remaining clips? (y/n): ")
                if response.lower() != 'y':
                    print("Stopping generation sequence.")
                    break

        print(f"\n✨ Generation sequence complete!")
        print(f"📁 Videos saved to: {OUTPUT_DIR}")
        print(f"📋 Metadata saved to: {METADATA_FILE}")


def main():
    """Main execution function"""

    # Initialize generator
    generator = VeoVideoGenerator(API_KEY)

    # Define clip generation sequence
    clips = [
        # Clip 1: Galileo (Independent)
        {
            "clip_id": "clip_1_galileo",
            "prompt": """Galileo Galilei stands at a brass telescope gazing upward at infinite starry night sky in 1610 Tuscany. Wide cinematic establishing shot emphasizing dramatic scale of cosmos above and single human figure below. Period-accurate Renaissance clothing, doublet and robe. Warm golden candlelight from nearby stone villa window illuminates his figure from side, mixing with cool blue starlight from above. His face shows pure wonder and awe looking upward at the heavens. Open Tuscan landscape with rolling hills barely visible in darkness. Camera is static wide shot, allowing the moment to breathe. Shot on 35mm film with warm color grading, Terrence Malick aesthetic. Shallow depth of field with stars in sharp focus and foreground slightly soft. Intimate spiritual moment of discovery between one man and infinite universe. Gentle night wind sounds, distant crickets, soft sound of telescope brass adjusting, breath of wonder. Warm renaissance lute music playing softly in background, period accurate and contemplative.""",
            "duration": 5,
            "resolution": "1080p"
        },

        # Clip 2: Time Collapse (Extend from Clip 1)
        {
            "clip_id": "clip_2_time_collapse",
            "prompt": """Same framing and camera position as previous shot. Rapid impressionistic time-lapse transition from 1610 to 2025. Starry sky overhead morphs into institutional fluorescent ceiling. Warm candlelight multiplies into harsh cold fluorescent office lights. Open Tuscan landscape closes into sterile university research lab walls. Single Renaissance figure dissolves and is replaced by crowds of people in modern lab coats. Telescope transforms into computer workstations. Natural wonder transitions into institutional work environment. Color grading shifts from warm golden candlelight tones to cold sterile blue-white fluorescent lighting. Camera remains locked in same position throughout showing the transformation. Ethereal whooshing time compression sound effect. Warm lute music becomes increasingly dissonant and distorted. Institutional sounds fade in: fluorescent light buzzing, computer fans humming, electronic door locks clicking. Transition from organic natural sounds to mechanical institutional sounds.""",
            "duration": 5,
            "resolution": "1080p",
            "extend_from_clip": "clip_1_galileo"
        },

        # Clip 3A: Terminal Errors (Independent - Montage)
        {
            "clip_id": "clip_3a_terminal_errors",
            "prompt": """Extreme close-up of computer terminal screen showing rapid scrolling red error messages. Text clearly visible: "ModuleNotFoundError: No module named 'tensorflow'", "CUDA installation failed", "ImportError", "RuntimeError". Black terminal background with bright red error text. Hands visible at bottom of frame typing frantically on keyboard. Cold blue screen light illuminating frustrated face partially visible reflected in screen. Fast frantic keyboard typing sounds, rapid error beeps, computer fan whirring loudly. Harsh fluorescent office lighting from above. Documentary-style handheld camera. Modern sterile research environment. 1 second duration, quick cut for montage sequence.""",
            "duration": 1,
            "resolution": "1080p"
        },

        # Clip 3B: Literature Overwhelm (Independent - Montage)
        {
            "clip_id": "clip_3b_literature_overwhelm",
            "prompt": """Medium shot of person at desk with laptop showing 47 browser tabs open at top. Screen filled with academic PDF papers stacked in multiple windows. Person's hands scrolling rapidly through research papers with mouse, clearly overwhelmed. Face shows exhaustion and information overload. Papers have titles visible with words like "Neural Networks", "Machine Learning", academic journal formatting. Multiple windows overlap chaotically. Cold blue laptop screen light. Messy desk with coffee cups and scattered printed papers. Frantic mouse clicking sounds, rapid scrolling sound, paper rustling. Fluorescent office buzz in background. Documentary close-up style. Modern research environment. 1 second duration for quick montage cut.""",
            "duration": 1,
            "resolution": "1080p"
        },

        # Clip 3C: GPU Queue (Independent - Montage)
        {
            "clip_id": "clip_3c_gpu_queue",
            "prompt": """Tight close-up of laptop screen showing GPU job queue interface. Large text visible on screen: "GPU Queue Position: 89" and "Estimated Wait Time: 14 hours 23 minutes". Progress bar barely moved, showing 3% complete. Cursor hovering helplessly over refresh button. Person's face partially visible reflected in screen showing disappointment and resignation. Cold blue laptop screen glow. Dark room lit only by screen. Queue number ticking sound, slow loading sound, disappointed sigh. Modern sterile environment. Static camera focused on screen. 1 second duration for rapid montage sequence.""",
            "duration": 1,
            "resolution": "1080p"
        },

        # Clip 3D: Environment Hell (Independent - Montage)
        {
            "clip_id": "clip_3d_environment_hell",
            "prompt": """Extreme close-up of hands rapidly typing terminal commands for environment setup. Screen visible showing terminal with commands: "pip install tensorflow", "conda create --name myenv", immediately followed by error messages in red text. Multiple overlapping terminal windows visible on screen showing configuration attempts. Package dependency conflicts visible: "Requires: python >=3.8, <3.9" conflicting with "Requires: python >=3.9". Hands showing frustration with rapid typing then stopping abruptly. Cold fluorescent lighting. Rapid keyboard mashing sounds, error beeps, frustrated exhale. Documentary-style tight framing. Modern research lab setting. 1 second duration for quick montage cut.""",
            "duration": 1,
            "resolution": "1080p"
        },

        # Clip 3E: Permission Denied (Independent - Montage)
        {
            "clip_id": "clip_3e_permission_denied",
            "prompt": """Close-up of laptop screen showing email inbox. Email subject lines clearly visible: "Grant Application Status: INSUFFICIENT CREDENTIALS", "Compute Cluster Access Request: DENIED", "Research Proposal: NOT APPROVED". Person clicking through emails with mouse, each one showing rejection. Red stamps or badges visible on emails indicating denial. Face partially reflected in screen showing defeat. Cold blue email interface light. Disappointing email notification "ding" sound, mouse clicking, heavy sigh. Sterile office environment. Static camera on screen. 1 second duration for rapid montage.""",
            "duration": 1,
            "resolution": "1080p"
        },

        # Clip 3F: Buried in Papers (Independent - Montage)
        {
            "clip_id": "clip_3f_buried_papers",
            "prompt": """Wide shot of person at desk completely surrounded and obscured by tall stacks of printed research papers. Only top of person's head visible behind paper towers. Papers stacked precariously high on all sides. Academic papers with visible titles and journal formatting. Cold fluorescent overhead lighting casting harsh shadows. Sense of isolation and being buried alive in literature. Overwhelming stacks create claustrophobic framing. Papers rustling and shuffling sounds, overwhelming ambience, oppressive silence. Documentary-style static wide shot. Modern sterile research office. 1 second duration for final montage cut.""",
            "duration": 1,
            "resolution": "1080p"
        },

        # Clip 4: Breaking Point (Independent)
        {
            "clip_id": "clip_4_breaking_point",
            "prompt": """Medium shot of person at desk stopping all activity. They sit back in chair with defeated posture, looking down at their hands with exhaustion. Face shows complete resignation and giving up. Harsh fluorescent office lighting from above. Cluttered desk with terminal errors still visible on screen. Person's eyes slowly close. Camera slowly zooms in on face showing emotional defeat. Cut to pure black screen. All sound cuts to silence except slow heavy exhausted breathing. Single slow heartbeat sound. Then complete silence. Hold the uncomfortable powerful silence. Intimate documentary style. Modern research environment transforming to pure darkness. 3 seconds duration allowing the moment to breathe.""",
            "duration": 3,
            "resolution": "1080p"
        },

        # Clip 5: Light Returns (Extend from Clip 4)
        {
            "clip_id": "clip_5_light_returns",
            "prompt": """Pure black screen. Warm golden amber light begins glowing at bottom of frame. Same person from previous shot, eyes still closed, face barely visible. Warm laptop screen glow gradually illuminates face from below, Caravaggio-style lighting from darkness. Eyes slowly open with changed expression: exhaustion transforms to curiosity then recognition. Face bathed in warm hopeful golden light contrasting with previous cold blue. Soft electronic hum sound, breath becoming lighter and more hopeful. Single pure piano note rings out clear and hopeful. Warm ambient pad begins with string sounds underneath. Intimate close-up. Spiritual awakening moment. Hope emerging from darkness. 4 seconds duration, allowing transformation to unfold naturally.""",
            "duration": 4,
            "resolution": "1080p",
            "extend_from_clip": "clip_4_breaking_point"
        },

        # Clip 6: Discovery Abstract (Independent)
        {
            "clip_id": "clip_6_discovery_abstract",
            "prompt": """Abstract visualization sequence showing discovery and understanding happening. NOT literal user interface. Artistic representations: dark blue ink dispersing organically in water representing ideas spreading. Neural network nodes lighting up in golden amber showing connections forming. Mathematical equations appearing and connecting with glowing lines showing understanding building. Data streams flowing like luminous rivers in space. Warm light refracting through prisms creating spectrum. All in Orchestra brand colors: warm blue (#0099FF) and amber gold tones. Fast paced but organic and alive, beautiful and flowing. No people visible, pure abstract visual poetry of discovery. Warm electronic ambient music building with hopeful restrained strings. Organic sounds mixed with digital: water flowing, light harmonics, gentle electronic pulses. Building emotional momentum but not bombastic. Terrence Malick meets abstract data visualization aesthetic. 6 seconds duration.""",
            "duration": 6,
            "resolution": "1080p"
        },

        # Clip 7: Constellation (Extend from Clip 6)
        {
            "clip_id": "clip_7_constellation",
            "prompt": """Pull back from previous abstract visuals to reveal concrete reality. Original person working at laptop, face illuminated by warm screen glow. Camera continues pulling back revealing they are not alone. Other people appear in darkness around them scattered at different distances. Each person illuminated by their own warm laptop screen glow in darkness. Different ages visible: teenagers, elderly person, parent with child nearby. Different locations: cozy home office, small apartment, cafe corner. Creating constellation pattern of warm lights in darkness like stars. All working peacefully, sense of quiet collective discovery. Wide shot revealing the emerging movement of curious people. Multiple keyboards typing creating rhythmic almost musical pattern. Warm strings swelling emotionally but remaining restrained. Collective breathing sounds. Sense of community and connection. Building toward manifesto moment. Cinematic wide shot. 5 seconds duration.""",
            "duration": 5,
            "resolution": "1080p",
            "extend_from_clip": "clip_6_discovery_abstract"
        }
    ]

    # Generate all clips in sequence
    generator.generate_sequence(clips)

    print("\n" + "="*60)
    print("🎬 All clips generated successfully!")
    print(f"📁 Output directory: {OUTPUT_DIR}")
    print(f"📋 Metadata file: {METADATA_FILE}")
    print("\nNext steps:")
    print("1. Review generated clips")
    print("2. Add text overlays in post-production")
    print("3. Stitch clips together")
    print("4. Final color grading and audio mixing")
    print("="*60)


if __name__ == "__main__":
    main()
