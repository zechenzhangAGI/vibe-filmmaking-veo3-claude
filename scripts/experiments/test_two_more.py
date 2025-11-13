#!/usr/bin/env python3
"""
Test script to generate two more clips: Time Collapse and Breaking Point
"""

import os
import sys
from dotenv import load_dotenv
from generate_videos import VeoVideoGenerator

load_dotenv()

def main():
    """Generate two test clips"""

    print("🧪 Orchestra Launch Video - Testing Clips 2 & 4")
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

    # Test Clip 4: Breaking Point (different style - darkness, emotion)
    print("📹 Test 1: Clip 4 - Breaking Point")
    print("   Duration: 4s")
    print("   Style: Intimate, darkness, silence as power")
    print()

    prompt_breaking = """Medium shot of person stopping all activity, sitting back defeated. Looking down at hands with exhaustion. Face shows complete resignation. Eyes slowly close. Camera slowly zooms into face. Cut to pure black screen. All sound cuts to silence except slow heavy breathing. Single slow heartbeat. Then complete silence. Hold the powerful silence. Intimate documentary style. Modern environment transforming to pure darkness."""

    try:
        result1 = generator.generate_clip(
            clip_id="test_clip_4_breaking_point_4s",
            prompt=prompt_breaking,
            duration=4,
            resolution="720p",
            aspect_ratio="16:9"
        )
        print(f"✅ Clip 4 generated: {result1['video_path']}")
        print()
    except Exception as e:
        print(f"❌ Failed: {e}")
        print()

    # Test Clip 6: Discovery Abstract (very different - abstract, colorful)
    print("📹 Test 2: Clip 6 - Discovery Abstract")
    print("   Duration: 6s")
    print("   Style: Abstract, visual poetry, warm colors")
    print()

    prompt_abstract = """Abstract cinematic visualization of discovery. NOT literal UI. Dark blue ink dispersing organically in water representing ideas spreading. Neural network nodes lighting up in golden amber showing connections forming. Mathematical equations appearing and connecting with glowing lines. Data streams flowing like luminous rivers in space. Warm light refracting through prisms. Orchestra brand colors - warm blue and amber gold tones. Fast paced but organic and alive, beautiful flowing. No people, pure visual poetry of discovery. Terrence Malick meets abstract data visualization. Warm electronic ambient music building with hopeful restrained strings. Organic sounds mixed with digital - water flowing, light harmonics, gentle electronic pulses. Building emotion but not bombastic."""

    try:
        result2 = generator.generate_clip(
            clip_id="test_clip_6_abstract_6s",
            prompt=prompt_abstract,
            duration=6,
            resolution="720p",
            aspect_ratio="16:9"
        )
        print(f"✅ Clip 6 generated: {result2['video_path']}")
        print()
    except Exception as e:
        print(f"❌ Failed: {e}")
        print()

    print("="*60)
    print("🎬 Test generation complete!")
    print()
    print("Generated clips:")
    print("1. Clip 4 (Breaking Point): Emotional, dark, silence")
    print("2. Clip 6 (Abstract): Visual poetry, colorful, no people")
    print()
    print("Review these to test different styles before full generation.")
    print("="*60)

if __name__ == "__main__":
    main()
