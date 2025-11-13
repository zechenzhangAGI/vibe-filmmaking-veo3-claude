#!/usr/bin/env python3
"""
Regenerate Scene 1 (Galileo Wonder) at 720p for video extension compatibility
Scene 1 at 1080p cannot be extended (Veo only supports 720p for extensions)
"""

import os
import sys
from dotenv import load_dotenv
from generate_videos import VeoVideoGenerator

load_dotenv()

def main():
    """Regenerate Scene 1 at 720p"""

    print("🎬 Regenerating Scene 1: Galileo's Wonder")
    print("   Resolution: 720p (for extension compatibility)")
    print("   Duration: 8s")
    print("   Style: Pencil sketch animation")
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

    # Check if 1080p version exists
    if "v5_test_clip_1_galileo_8s" in generator.metadata.get("clips", {}):
        print("ℹ️  Note: 1080p version already exists")
        print("   Generating new 720p version with different clip_id")
        print()

    # Scene 1: Galileo Wonder - 720p for extension
    print("📹 Scene 1: Galileo's Wonder (720p)")
    print("   This version can be extended with Scene 1B")
    print()

    prompt = """Subject: Galileo figure at telescope under starry night sky. Action: Looking through telescope eyepiece, then slowly lifting head upward to gaze at stars with wonder, subtle head tilt, contemplative breathing. Style: Pencil sketch animation, hand-drawn loose gestural lines, charcoal shading, expressive artistic sketch aesthetic, visible pencil strokes, animated drawing quality. Camera: Slow dolly in from wide to medium shot, gentle camera push emphasizing intimacy. Composition: Starting wide shot emphasizing scale - vast cosmos above small figure below, ending medium shot showing face. Focus: Sketch-like focus with hand-drawn quality, stars sketched with radiating lines. Ambiance: Warm golden candlelight from stone villa window mixing with cool blue starlight, intimate night atmosphere, sketched light rays. Audio: Gentle night breeze, distant crickets chirping softly, telescope adjusting, breath of wonder, soft contemplative music building."""

    try:
        result = generator.generate_clip(
            clip_id="scene_1_galileo_720p_8s",
            prompt=prompt,
            duration=8,
            resolution="720p",
            aspect_ratio="16:9"
        )

        print()
        print("="*60)
        print("🎉 SUCCESS! Scene 1 (720p) generated!")
        print("="*60)
        print()
        print(f"📋 Clip Details:")
        print(f"   ID: {result['clip_id']}")
        print(f"   Resolution: 720p (extension-compatible)")
        print(f"   Video Path: {result['video_path']}")
        print(f"   Generation Time: {result.get('generation_time_seconds', 'N/A')}s")
        print()
        print("🎬 Next step:")
        print("   Review this 720p version")
        print("   If approved, run generate_scene_1b_discovery_joy.py")
        print("   to extend with Scene 1B (discovery joy)")
        print("="*60)

    except Exception as e:
        print()
        print("="*60)
        print("❌ FAILED to generate Scene 1 (720p)")
        print("="*60)
        print()
        print(f"Error: {str(e)}")
        print()
        print("Troubleshooting:")
        print("1. Check API key and connection")
        print("2. Verify rate limits")
        print("3. Check API status")
        sys.exit(1)

if __name__ == "__main__":
    main()
