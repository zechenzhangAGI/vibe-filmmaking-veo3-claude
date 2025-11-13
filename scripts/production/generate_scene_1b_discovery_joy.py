#!/usr/bin/env python3
"""
Generate Scene 1B: Discovery Joy
Extends from scene_1_galileo_720p_8s (720p version for extension compatibility)
Shows Galileo's eureka moment and joyful sketching
"""

import os
import sys
from dotenv import load_dotenv
from generate_videos import VeoVideoGenerator

load_dotenv()

def main():
    """Generate Scene 1B extending from Scene 1"""

    print("🎬 Generating Scene 1B: Discovery Joy")
    print("   Extends from: scene_1_galileo_720p_8s")
    print("   Style: Pencil sketch animation")
    print("   Resolution: 720p, 16:9 (extension requirement)")
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

    # Check that Scene 1 (720p) exists
    if "scene_1_galileo_720p_8s" not in generator.metadata.get("clips", {}):
        print("❌ Error: Scene 1 (scene_1_galileo_720p_8s) not found!")
        print("   You need to generate Scene 1 at 720p first using regenerate_scene_1_720p.py")
        sys.exit(1)

    print("✅ Scene 1 found, ready to extend")
    print()

    # Scene 1B: Discovery Joy - EXTENDS from Scene 1
    print("📹 Scene 1B: Discovery Joy (Eureka Moment)")
    print("   Action: Realization → Pull back → Grab notebook → Sketch discovery")
    print("   Emotion: Pure joy, intellectual excitement")
    print()

    prompt = """Subject: Same Galileo figure from previous scene, still at telescope. Action: Face suddenly lights up with realization and joy - eureka moment seeing Jupiter's moons, pulls back from telescope excitedly looking up at sky with naked eye, reaches for nearby notebook on table, opens it eagerly, begins sketching circles enthusiastically (Jupiter with moons orbiting), hand drawing animated sketch lines appearing on paper, expression showing pure intellectual joy. Style: Pencil sketch animation, hand-drawn loose gestural lines with extra emphasis on the sketch-within-sketch (notebook drawings), charcoal shading, expressive joyful energy in line work, visible excited pencil strokes, animated drawing quality showing discovery in action. Camera: Medium shot continuing from previous clip, slight push in on face during realization moment, then pulls back slightly to reveal notebook and sketching action, intimate framing maintaining connection. Composition: Medium shot of Galileo, telescope visible, notebook becomes prominent in frame as he sketches, candlelight illuminating both face and paper. Focus: Sketch focus on face during realization, then splits focus between hand sketching and joyful expression, hand-drawn quality throughout. Ambiance: Same warm golden candlelight from villa window, cool blue starlight, sketched light rays, warm intimate atmosphere intensifies with joy, animated sketch lines on notebook paper glow slightly with discovery energy. Audio: Excited breath with "Ah!" of realization, telescope movement as pulls back from eyepiece, excited rustling of notebook pages, quill scratching on paper enthusiastically with rhythm, lute music swells with joy and wonder building emotionally, night wind and crickets continue, pure happiness in soundscape."""

    try:
        result = generator.generate_clip(
            clip_id="scene_1b_discovery_joy_720p_8s",
            prompt=prompt,
            duration=8,
            resolution="720p",
            aspect_ratio="16:9",
            extend_from_clip="scene_1_galileo_720p_8s"  # EXTEND from Scene 1 (720p)!
        )

        print()
        print("="*60)
        print("🎉 SUCCESS! Scene 1B generated!")
        print("="*60)
        print()
        print(f"📋 Clip Details:")
        print(f"   ID: {result['clip_id']}")
        print(f"   Extended from: Scene 1 (Galileo)")
        print(f"   Video Path: {result['video_path']}")
        print(f"   Generation Time: {result.get('generation_time_seconds', 'N/A')}s")
        print()
        print("📝 What this shows:")
        print("   - Eureka moment (face lights up)")
        print("   - Pull back from telescope")
        print("   - Grab notebook excitedly")
        print("   - Sketch Jupiter's moons with joy")
        print("   - Pure unencumbered discovery")
        print()
        print("🎬 Next step:")
        print("   Review Scene 1B to verify it captures the joy of discovery")
        print("   Then generate Scene 2 (Time Collapse) extending from Scene 1B")
        print("="*60)

    except Exception as e:
        print()
        print("="*60)
        print("❌ FAILED to generate Scene 1B")
        print("="*60)
        print()
        print(f"Error: {str(e)}")
        print()
        print("Troubleshooting:")
        print("1. Make sure Scene 1 was generated successfully")
        print("2. Check that the video file exists")
        print("3. Verify API key and connection")
        sys.exit(1)

if __name__ == "__main__":
    main()
