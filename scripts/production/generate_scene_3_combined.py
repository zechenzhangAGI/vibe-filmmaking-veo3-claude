#!/usr/bin/env python3
"""
Generate Scene 3: Combined Infrastructure Hell Montage
All 6 frustrations in one shot using split-screen panels
Progressive escalation: 1→2→4→6 panels building to climax
"""

import os
import sys
from dotenv import load_dotenv
from generate_videos import VeoVideoGenerator

load_dotenv()

def main():
    """Generate Scene 3 Combined Montage"""

    print("🎬 Generating Scene 3: Combined Infrastructure Hell")
    print("   Style: Split-screen panels building 1→2→4→6")
    print("   Pencil sketch animation")
    print("   Resolution: 1080p, 16:9")
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

    # Scene 3: Combined montage
    print("📹 Scene 3: Combined Infrastructure Hell Montage")
    print("   All 6 frustrations in progressive split-screen")
    print("   Terminal → Literature → GPU Queue → Environment → Permission → Papers")
    print()

    prompt = """Subject: Computer screens and desk workspace showing cascading digital frustrations through expanding split-screen panels
Action: Opens extreme close-up on single terminal screen with red error messages scrolling rapidly, hands typing frantically at bottom edge entering commands desperately. At 2 seconds, screen SPLITS vertically - left panel continues terminal errors, right panel reveals browser with 47 tabs visible and cursor scrolling frantically through PDFs and papers. At 3 seconds, splits into 4-panel grid: top-left terminal errors persist, top-right browser chaos continues, bottom-left GPU queue appears showing "Position 89 | Wait: 14 hours" with cursor clicking refresh button repeatedly, bottom-right environment setup terminal with "pip install", "conda create", "ModuleNotFoundError" cascading. At 5 seconds, expands to 6 panels adding fifth panel with email inbox showing "ACCESS DENIED", "INSUFFICIENT CREDENTIALS", "Grant Request: DENIED" messages with cursor clicking through rejections hopelessly, sixth panel shows overhead view of desk with tall paper stacks, scattered documents, notebook buried under papers, hands shuffling papers helplessly. Final 2 seconds all 6 panels active simultaneously in chaotic motion - typing, scrolling, clicking, refreshing, papers rustling - building to crescendo, then hands in terminal panel suddenly stop typing and pull back slowly in surrender, other hands cease motion, cursors stop, stillness spreads across all panels showing defeat.
Style: Pencil sketch animation throughout all panels, bold sketchy lines for text and interface elements, dynamic gestural hand-drawn quality, progressive visual intensity with heavier charcoal shading as panels multiply, expressive chaotic line work, visible aggressive pencil strokes creating mounting overwhelming tension, each panel maintains consistent hand-drawn aesthetic
Camera: Opens tight extreme close-up on single screen establishing intimacy with problem, holds steady as panels split and multiply creating expanding visual field, subtle slow zoom out in final 2 seconds revealing full 6-panel grid scope, smooth continuous framing capturing all panel activity simultaneously
Composition: Begins single full-frame terminal screen, progressively splits into organized grid (1→2 vertical split→4 grid→6 panels), clear sketched panel borders separating each frustration, balanced grid layout with equal panel sizes, ending wide enough to show complete 6-panel array with all activity visible, visual progression from focused to fragmented to overwhelming
Focus: Sharp sketch focus on text, hands, and cursors within each panel as it appears and activates, all panels remain in focus showing simultaneous chaos, hand-drawn details clear in typing hands and error messages, energetic sketch line work maintains clarity despite mounting visual complexity
Ambiance: Cold blue screen glows sketched with harsh cross-hatching emanating from all monitor panels, multiple overlapping blue light sources creating oppressive multi-directional illumination, dark shadows between panels sketched with heavy charcoal, claustrophobic atmosphere of being surrounded by glowing failure screens, fluorescent overhead lighting sketched with parallel hatching lines adding cold institutional quality, papers in sixth panel lit by harsh overhead creating deep shadows
Audio: Terminal error beeps rapid and persistent, frantic keyboard typing accelerating, browser panel adds mouse clicking frantically and scrolling sounds, GPU queue adds repetitive refresh click and ominous clock ticking, environment terminal adds aggressive keyboard mashing and error beep acceleration, email panel adds disappointing notification dings repeating, paper panel adds heavy rustling and stack shifting sounds - ALL AUDIO SOURCES LAYERING SIMULTANEOUSLY building to oppressive cacophony of failure sounds, fluorescent lights buzzing steadily underneath everything, building to peak chaos then sudden shift to isolated typing slowing, final key press, silence spreading as motion stops, just fluorescent buzz and breathing remaining"""

    try:
        result = generator.generate_clip(
            clip_id="scene_3_combined_montage_1080p_8s",
            prompt=prompt,
            duration=8,
            resolution="1080p",
            aspect_ratio="16:9"
        )

        print()
        print("="*60)
        print("🎉 SUCCESS! Scene 3 Combined Montage generated!")
        print("="*60)
        print()
        print(f"📋 Clip Details:")
        print(f"   ID: {result['clip_id']}")
        print(f"   Video Path: {result['video_path']}")
        print(f"   Generation Time: {result.get('generation_time_seconds', 'N/A')}s")
        print()
        print("📝 What this shows:")
        print("   - Progressive split: 1→2→4→6 panels")
        print("   - All 6 frustrations building simultaneously")
        print("   - Terminal errors → Literature → GPU → Environment → Permission → Papers")
        print("   - Climax: All panels active in chaotic cacophony")
        print("   - Resolution: Hands stop, defeat spreads across all panels")
        print()
        print("🎬 Next step:")
        print("   Review Scene 3 combined montage")
        print("   Then generate Scene 4 (Breaking Point)")
        print("="*60)

    except Exception as e:
        print()
        print("="*60)
        print("❌ FAILED to generate Scene 3")
        print("="*60)
        print()
        print(f"Error: {str(e)}")
        print()
        print("Troubleshooting:")
        print("1. Check API key and connection")
        print("2. Verify quota available")
        print("3. Check network connection")
        sys.exit(1)

if __name__ == "__main__":
    main()
