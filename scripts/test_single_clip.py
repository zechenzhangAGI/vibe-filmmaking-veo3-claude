#!/usr/bin/env python3
"""
Test script to generate a single clip with Veo 3.1
Use this to test API connectivity and prompt quality before generating all clips.
"""

import os
import sys
from dotenv import load_dotenv
from generate_videos import VeoVideoGenerator

# Load environment variables
load_dotenv()

def main():
    """Generate a single test clip"""

    print("🧪 Orchestra Launch Video - Single Clip Test")
    print("="*60)

    # Check API key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ Error: GOOGLE_API_KEY not found in .env file")
        print("\nPlease:")
        print("1. Open scripts/.env")
        print("2. Add your Google API key: GOOGLE_API_KEY=your_key_here")
        print("3. Save and run again")
        sys.exit(1)

    print(f"✅ API key loaded (length: {len(api_key)} chars)")
    print()

    # Initialize generator
    try:
        generator = VeoVideoGenerator(api_key)
        print("✅ Generator initialized")
        print()
    except Exception as e:
        print(f"❌ Failed to initialize generator: {e}")
        sys.exit(1)

    # Test clip: Galileo (4s minimum for Veo 3.1)
    print("📹 Generating test clip: Galileo opening scene")
    print("   Duration: 4s (minimum for Veo 3.1)")
    print("   Model: veo-3.1-generate-preview")
    print()

    # V4 ANIMATED PROMPT - Paper cut-out animation style for artistic taste
    test_prompt = """Subject: Galileo figure at telescope under starry night sky. Action: Gazing upward at stars, static contemplative pose. Style: Paper cut-out animation with layered depth, handmade aesthetic, textured paper layers. Camera: Static wide shot. Composition: Wide shot emphasizing scale - vast cosmos above, small figure below. Focus: Deep focus showing both figure and stars. Ambiance: Warm golden candlelight from window mixing with cool blue starlight, intimate night atmosphere. Audio: Gentle night breeze, distant crickets chirping softly, soft contemplative music."""

    try:
        result = generator.generate_clip(
            clip_id="test_clip_galileo_v4_animated_4s",
            prompt=test_prompt,
            duration=4,  # Minimum duration for Veo 3.1 is 4 seconds
            resolution="720p",  # 1080p requires 8s, using 720p for faster test
            aspect_ratio="16:9"
        )

        print()
        print("="*60)
        print("🎉 SUCCESS! Test clip generated")
        print("="*60)
        print()
        print(f"📋 Clip Details:")
        print(f"   ID: {result['clip_id']}")
        print(f"   Duration: {result['duration']}s")
        print(f"   Resolution: {result['resolution']}")
        print(f"   Video Path: {result['video_path']}")
        print(f"   Generation Time: {result.get('generation_time_seconds', 'N/A')}s")
        print(f"   Generated: {result.get('generated_at', 'N/A')}")
        print()
        print("📁 Metadata saved to: output/generation_metadata.json")
        print()
        print("Next steps:")
        print("1. Review the generated clip quality")
        print("2. If satisfied, run: python generate_videos.py")
        print()

    except Exception as e:
        print()
        print("="*60)
        print("❌ FAILED to generate test clip")
        print("="*60)
        print()
        print(f"Error: {str(e)}")
        print()
        print("Troubleshooting:")
        print("1. Check API key is correct in .env")
        print("2. Verify Veo 3.1 API access is enabled in Google Cloud Console")
        print("3. Ensure you're using the correct Google GenAI SDK")
        print("4. Check you have proper billing set up")
        print("5. Review error message above")
        print()
        sys.exit(1)

if __name__ == "__main__":
    main()
