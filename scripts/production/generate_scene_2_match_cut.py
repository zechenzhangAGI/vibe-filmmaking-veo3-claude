#!/usr/bin/env python3
"""
Generate Scene 2: Match Cut to Modern Science
Extends from scene_1b_720p.mp4 (720p version for extension compatibility)
Shows match cut from Galileo sketching → Modern researcher typing
"""

import os
import sys
from dotenv import load_dotenv
from generate_videos import VeoVideoGenerator

load_dotenv()

def main():
    """Generate Scene 2 extending from Scene 1B"""

    print("🎬 Generating Scene 2: Match Cut to Modern Science")
    print("   Extends from: scene_1b_720p")
    print("   Style: Pencil sketch animation")
    print("   Resolution: 720p, 16:9")
    print("   Duration: 8s")
    print("="*60)

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ Error: GOOGLE_API_KEY not found")
        sys.exit(1)

    print(f"✅ API key loaded")
    print()

    try:
        generator = VeoVideoGenerator(api_key)
        print("✅ Generator initialized")
        print()
    except Exception as e:
        print(f"❌ Failed to initialize: {e}")
        sys.exit(1)

    # First, we need to add scene_1b_720p to metadata manually since it was converted
    # Check if it exists as a file
    from pathlib import Path
    output_dir = Path(__file__).parent.parent / "output"
    scene_1b_path = output_dir / "scene_1b_720p.mp4"

    if not scene_1b_path.exists():
        print("❌ Error: scene_1b_720p.mp4 not found!")
        print(f"   Expected at: {scene_1b_path}")
        sys.exit(1)

    print(f"✅ Found Scene 1B (720p): {scene_1b_path.name}")

    # Add it to metadata if not already there
    if "scene_1b_720p" not in generator.metadata.get("clips", {}):
        print("📝 Adding scene_1b_720p to metadata...")
        generator.metadata["clips"]["scene_1b_720p"] = {
            "clip_id": "scene_1b_720p",
            "video_path": str(scene_1b_path),
            "video_filename": "scene_1b_720p.mp4",
            "resolution": "720p",
            "duration": 8,
            "aspect_ratio": "16:9"
        }
        generator._save_metadata()
        print("✅ Metadata updated")

    print()

    # Scene 2: Match Cut - EXTENDS from Scene 1B
    print("📹 Scene 2: Match Cut to Institutional Bureaucracy")
    print("   Transition: Hands sketching in notebook → Hands writing in notebook")
    print("   Emotion: Joy of discovery → Bureaucratic drudgery")
    print()

    prompt = """Subject: Modern researcher's hand writing in physical notebook at desk, surrounded by bureaucratic institutional laboratory setting
Action: Close-up on hand writing data into lined notebook with pen (directly mirroring Galileo's sketching hand gesture and composition), filling out forms and recording routine observations methodically, camera slowly pulls back revealing researcher at desk in sterile institutional laboratory, multiple identical desks visible with other researchers in lab coats doing similar repetitive paperwork tasks, all heads down filling forms and clipboards, researcher pauses writing to look up at institutional clock on wall showing late hour, glances around at rows of colleagues doing identical tasks, returns to form-filling with resigned mechanical motion, no joy or discovery - pure bureaucratic routine
Style: Pencil sketch animation maintaining identical hand-drawn aesthetic from previous scene, sketchy lines for modern institutional architecture and equipment, charcoal shading creating harsh shadows under cold fluorescent lights, visible pencil strokes showing repetitive patterns and institutional conformity, hand-drawn quality emphasizing loss of individuality
Camera: Opens with exact same tight composition on hand writing in notebook as previous scene's sketching hands, slow steady pull back revealing first the researcher, then progressively more of the crowded institutional space with many identical workstations, settles on wide shot showing rows of researchers doing identical bureaucratic tasks
Composition: Opening frame precisely mirrors Galileo's hand sketching in notebook - same angle, same gesture of hand with writing instrument and notebook, camera reveals the devastating contrast as it pulls back showing institutional uniformity replacing individual discovery, same pencil sketch visual language but with oppressive repetitive patterns and darker shading
Focus: Sharp sketch focus on hand writing data in notebook, transitions to split focus showing both individual researcher and the crowd of identical workers, hand-drawn quality emphasizes dehumanization through institutional conformity and loss of personal discovery
Ambiance: Cold blue-white fluorescent tube lighting sketched with harsh parallel hatching lines creating oppressive uniform overhead illumination, no warmth or candlelight - only sterile institutional brightness, heavy shadows under desks and equipment, claustrophobic despite large open laboratory floor, institutional clock prominent on wall, beige walls and gray desks, atmosphere of bureaucratic conformity
Audio: Pen scratching on paper (mechanical, repetitive - contrasts with Galileo's excited sketching), rustling of forms and clipboards, fluorescent lights buzzing overhead in steady hum, institutional clock ticking loudly, multiple pens writing simultaneously creating rhythmic repetitive sound, papers shuffling, chairs creaking, muffled institutional announcements, HVAC system steady drone, no music - just bureaucratic ambient sound creating atmosphere of routine drudgery, complete contrast to previous scene's organic warmth and joyful discovery"""

    try:
        result = generator.generate_clip(
            clip_id="scene_2_match_cut_720p_8s",
            prompt=prompt,
            duration=8,
            resolution="720p",
            aspect_ratio="16:9",
            extend_from_clip="scene_1b_720p"  # EXTEND from Scene 1B (720p)!
        )

        print()
        print("="*60)
        print("🎉 SUCCESS! Scene 2 generated!")
        print("="*60)
        print()
        print(f"📋 Clip Details:")
        print(f"   ID: {result['clip_id']}")
        print(f"   Extended from: Scene 1B (720p)")
        print(f"   Video Path: {result['video_path']}")
        print(f"   Generation Time: {result.get('generation_time_seconds', 'N/A')}s")
        print()
        print("📝 What this shows:")
        print("   - Match cut: Hands sketching in notebook → Hands writing in notebook")
        print("   - Environment: Warm villa → Cold institutional lab")
        print("   - Emotion: Joy of discovery → Bureaucratic drudgery")
        print("   - Individual discovery → Institutional conformity")
        print("   - Many researchers doing identical repetitive tasks")
        print()
        print("🎬 Next step:")
        print("   Review Scene 2 match cut transition")
        print("   Then generate montage scenes (3A-3F)")
        print("="*60)

    except Exception as e:
        print()
        print("="*60)
        print("❌ FAILED to generate Scene 2")
        print("="*60)
        print()
        print(f"Error: {str(e)}")
        print()
        print("Troubleshooting:")
        print("1. Make sure Scene 1B (720p) was added to metadata")
        print("2. Check that the video file exists")
        print("3. Verify API key and connection")
        sys.exit(1)

if __name__ == "__main__":
    main()
