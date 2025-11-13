#!/usr/bin/env python3
"""
Test V5 Final: First few scenes with pencil sketch style at 1080p/8s
"""

import os
import sys
from dotenv import load_dotenv
from generate_videos import VeoVideoGenerator

load_dotenv()

def main():
    """Generate first 3 test clips with V5 final prompts"""

    print("🎬 Orchestra V5 Final - Testing First Scenes")
    print("   Style: Pencil sketch animation")
    print("   Resolution: 1080p, 16:9")
    print("   Duration: 8s per clip")
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

    # Test first 3 clips independently (not using extend yet)
    clips = [
        {
            "name": "Clip 1: Galileo Wonder",
            "clip_id": "v5_test_clip_1_galileo_8s",
            "prompt": """Subject: Galileo figure at telescope under starry night sky. Action: Looking through telescope eyepiece, then slowly lifting head upward to gaze at stars with wonder, subtle head tilt, contemplative breathing. Style: Pencil sketch animation, hand-drawn loose gestural lines, charcoal shading, expressive artistic sketch aesthetic, visible pencil strokes, animated drawing quality. Camera: Slow dolly in from wide to medium shot, gentle camera push emphasizing intimacy. Composition: Starting wide shot emphasizing scale - vast cosmos above small figure below, ending medium shot showing face. Focus: Sketch-like focus with hand-drawn quality, stars sketched with radiating lines. Ambiance: Warm golden candlelight from stone villa window mixing with cool blue starlight, intimate night atmosphere, sketched light rays. Audio: Gentle night breeze, distant crickets chirping softly, telescope adjusting, breath of wonder, soft contemplative music building.""",
            "duration": 8,
            "resolution": "1080p"
        },
        {
            "name": "Clip 3A: Terminal Errors",
            "clip_id": "v5_test_clip_3a_terminal_8s",
            "prompt": """Subject: Computer terminal screen with error messages and hands typing. Action: Hands typing frantically, error text scrolling rapidly upward, hands hitting keys harder with frustration, finally hands stopping and pulling back. Style: Pencil sketch animation, bold sketchy lines for text and hands, dynamic gestural drawing. Camera: Slow push in on screen, then slight shake conveying frustration. Composition: Extreme close-up of terminal screen with hands at bottom. Focus: Sharp sketch focus on error text and hand movements. Ambiance: Cold blue screen glow sketched with hatching, dark moody atmosphere with heavy shading. Audio: Rapid error beeps, keyboard typing frantically getting louder, frustrated exhale, low piano note begins.""",
            "duration": 8,
            "resolution": "1080p"
        },
        {
            "name": "Clip 4: Breaking Point",
            "clip_id": "v5_test_clip_4_breaking_8s",
            "prompt": """Subject: Person at desk working. Action: Typing slows then stops completely, hands lift from keyboard, person sits back heavily in chair, looks down at hands turning them over, eyes close slowly, head drops slightly, then fade to pure black screen. Style: Pencil sketch animation, loose emotional gestural lines, charcoal shading showing exhaustion, expressive hand-drawn vulnerability, sketch lines fading to black. Camera: Slow zoom from medium shot to intimate close-up on face showing defeat, smooth continuous push in, then cut to black. Composition: Medium shot transitioning to close-up portrait, ending in darkness. Focus: Shallow sketch focus on face with background fading, emotional pencil work. Ambiance: Harsh overhead lighting sketched with hard lines fading to pure black, darkness consuming the frame. Audio: Typing slowing down, keyboard final key press, chair creaking as lean back, all sound cutting to silence except slow heavy breathing, single heartbeat, then complete powerful silence.""",
            "duration": 8,
            "resolution": "1080p"
        }
    ]

    for i, clip in enumerate(clips, 1):
        print(f"\n{'='*60}")
        print(f"📹 Test {i}/{len(clips)}: {clip['name']}")
        print(f"{'='*60}\n")

        try:
            result = generator.generate_clip(
                clip_id=clip['clip_id'],
                prompt=clip['prompt'],
                duration=clip['duration'],
                resolution=clip['resolution'],
                aspect_ratio="16:9"
            )
            print(f"✅ {clip['name']} generated!")
            print(f"   Path: {result['video_path']}")
            print(f"   Time: {result.get('generation_time_seconds', 'N/A')}s")
            print()
        except Exception as e:
            print(f"❌ {clip['name']} failed: {e}")
            print()

    print("="*60)
    print("🎨 V5 Test Complete!")
    print()
    print("Review these 3 clips to verify:")
    print("1. Pencil sketch style looks good")
    print("2. Motion is present (camera + characters)")
    print("3. 1080p quality is satisfactory")
    print()
    print("If approved, run generate_videos_v5_final.py for all clips!")
    print("="*60)

if __name__ == "__main__":
    main()
