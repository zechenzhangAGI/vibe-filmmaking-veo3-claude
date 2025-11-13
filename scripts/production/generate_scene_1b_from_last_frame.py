#!/usr/bin/env python3
"""
Generate Scene 1B: Discovery Joy using last frame from Scene 1A
Uses image-to-video generation instead of extension to maintain 1080p quality
"""

import os
import sys
import subprocess
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types
import time

load_dotenv()

def extract_last_frame(video_path: str, output_path: str):
    """Extract the last frame from a video using ffmpeg as PNG"""
    print(f"📸 Extracting last frame from {Path(video_path).name}...")

    # Get video duration
    duration_cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        video_path
    ]

    try:
        duration = float(subprocess.check_output(duration_cmd).decode().strip())
        print(f"   Video duration: {duration:.2f}s")

        # Extract EXACT last frame as PNG (lossless)
        extract_time = max(0, duration - 0.04)  # One frame before end at 24fps

        extract_cmd = [
            "ffmpeg", "-y",
            "-ss", str(extract_time),
            "-i", video_path,
            "-frames:v", "1",
            "-f", "image2",
            "-pix_fmt", "rgb24",  # Ensure consistent pixel format
            output_path
        ]

        subprocess.run(extract_cmd, check=True, capture_output=True)
        print(f"✅ Last frame extracted to {Path(output_path).name}")
        return True

    except Exception as e:
        print(f"❌ Failed to extract frame: {e}")
        return False

def main():
    """Generate Scene 1B from last frame of Scene 1A"""

    print("🎬 Generating Scene 1B: Discovery Joy")
    print("   Method: Image-to-video from last frame of Scene 1A")
    print("   Resolution: 1080p, 16:9")
    print("   Duration: 8s")
    print("="*60)

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ Error: GOOGLE_API_KEY not found")
        sys.exit(1)

    print(f"✅ API key loaded")
    print()

    # Setup paths
    output_dir = Path(__file__).parent.parent / "output"
    scene_1a_path = output_dir / "v5_test_clip_1_galileo_8s.mp4"
    last_frame_path = output_dir / "scene_1a_last_frame.png"

    # Check Scene 1A exists
    if not scene_1a_path.exists():
        print(f"❌ Error: Scene 1A not found at {scene_1a_path}")
        sys.exit(1)

    print(f"✅ Found Scene 1A: {scene_1a_path.name}")
    print()

    # Extract last frame
    if not extract_last_frame(str(scene_1a_path), str(last_frame_path)):
        sys.exit(1)

    print()

    # Initialize Veo client
    try:
        client = genai.Client(api_key=api_key)
        print("✅ Veo client initialized")
        print()
    except Exception as e:
        print(f"❌ Failed to initialize: {e}")
        sys.exit(1)

    # Scene 1B prompt
    print("📹 Generating Scene 1B from last frame...")
    print()

    prompt = """Subject: Same Galileo figure from previous scene, still at telescope. Action: Face suddenly lights up with realization and joy - eureka moment seeing Jupiter's moons, pulls back from telescope excitedly looking up at sky with naked eye, reaches for nearby notebook on table, opens it eagerly, begins sketching circles enthusiastically (Jupiter with moons orbiting), hand drawing animated sketch lines appearing on paper, expression showing pure intellectual joy. Style: Pencil sketch animation, hand-drawn loose gestural lines with extra emphasis on the sketch-within-sketch (notebook drawings), charcoal shading, expressive joyful energy in line work, visible excited pencil strokes, animated drawing quality showing discovery in action. Camera: Medium shot continuing from previous clip, slight push in on face during realization moment, then pulls back slightly to reveal notebook and sketching action, intimate framing maintaining connection. Composition: Medium shot of Galileo, telescope visible, notebook becomes prominent in frame as he sketches, candlelight illuminating both face and paper. Focus: Sketch focus on face during realization, then splits focus between hand sketching and joyful expression, hand-drawn quality throughout. Ambiance: Same warm golden candlelight from villa window, cool blue starlight, sketched light rays, warm intimate atmosphere intensifies with joy, animated sketch lines on notebook paper glow slightly with discovery energy. Audio: Excited breath with "Ah!" of realization, telescope movement as pulls back from eyepiece, excited rustling of notebook pages, quill scratching on paper enthusiastically with rhythm, lute music swells with joy and wonder building emotionally, night wind and crickets continue, pure happiness in soundscape."""

    try:
        # Load the exact last frame as a Part
        print("📤 Loading exact last frame from Scene 1A...")

        # Read image as bytes
        with open(last_frame_path, 'rb') as f:
            image_bytes = f.read()

        print(f"✅ Image loaded: {len(image_bytes)} bytes")

        # Create a Part from the raw image bytes
        # This preserves the EXACT frame without any processing
        image_part = types.Part.from_bytes(
            data=image_bytes,
            mime_type="image/png"
        )

        # Pass through Gemini to get proper format
        # Gemini will echo back the EXACT image in proper format
        print("🔄 Processing through Gemini to get proper format...")
        temp_response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=[image_part, "Echo this image back"]
        )

        # The first part should be the image echoed back
        final_image = temp_response.parts[0].as_image() if hasattr(temp_response.parts[0], 'as_image') else temp_response.parts[0]
        print(f"✅ Image formatted for Veo")

        print(f"✅ Image part created")
        print()

        # Generate video directly from the raw image part
        print("🎬 Sending request to Veo 3.1 API with exact last frame...")
        config = types.GenerateVideosConfig(
            duration_seconds=8,
            resolution="1080p",
            aspect_ratio="16:9",
            number_of_videos=1
        )

        operation = client.models.generate_videos(
            model="veo-3.1-generate-preview",
            prompt=prompt,
            config=config,
            image=final_image
        )

        print("⏳ Waiting for video generation to complete...")
        print("   (This can take 10 seconds to 6 minutes)")

        # Poll for completion
        poll_count = 0
        while not operation.done:
            time.sleep(10)
            poll_count += 1
            print(f"   Still generating... ({poll_count * 10}s elapsed)")
            operation = client.operations.get(operation)

        # Download the generated video
        generated_video = operation.response.generated_videos[0]
        video_path = output_dir / "scene_1b_discovery_joy_1080p_8s.mp4"

        print(f"⬇️  Downloading generated video...")
        client.files.download(file=generated_video.video)
        generated_video.video.save(str(video_path))

        print()
        print("="*60)
        print("🎉 SUCCESS! Scene 1B generated!")
        print("="*60)
        print()
        print(f"📋 Clip Details:")
        print(f"   ID: scene_1b_discovery_joy_1080p_8s")
        print(f"   Method: Image-to-video from Scene 1A last frame")
        print(f"   Resolution: 1080p")
        print(f"   Video Path: {video_path}")
        print(f"   Generation Time: {poll_count * 10}s")
        print()
        print("📝 What this shows:")
        print("   - Eureka moment (face lights up)")
        print("   - Pull back from telescope")
        print("   - Grab notebook excitedly")
        print("   - Sketch Jupiter's moons with joy")
        print("   - Pure unencumbered discovery")
        print()
        print("🎬 Next step:")
        print("   Review Scene 1B")
        print("   Both clips can be stitched in post-production")
        print("="*60)

    except Exception as e:
        print()
        print("="*60)
        print("❌ FAILED to generate Scene 1B")
        print("="*60)
        print()
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
