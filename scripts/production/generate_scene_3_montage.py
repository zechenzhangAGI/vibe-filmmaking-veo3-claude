#!/usr/bin/env python3
"""
Generate Scene 3 Montage: 3A-3F
Infrastructure Hell - 6 individual clips
"""

import os
import sys
from dotenv import load_dotenv
from generate_videos import VeoVideoGenerator

load_dotenv()

def main():
    """Generate Scene 3 montage clips 3A-3F"""

    API_KEY = os.getenv("GOOGLE_API_KEY")
    if not API_KEY:
        print("❌ Error: GOOGLE_API_KEY not found")
        sys.exit(1)

    generator = VeoVideoGenerator(API_KEY)

    clips = [
        # Clip 3A: Terminal Errors - 8s, 1080p
        {
            "clip_id": "scene_3a_terminal_errors_1080p_8s",
            "prompt": """Subject: Computer terminal screen with error messages and hands typing. Action: Hands typing frantically, error text scrolling rapidly upward, hands hitting keys harder with frustration, finally hands stopping and pulling back. Style: Pencil sketch animation, bold sketchy lines for text and hands, dynamic gestural drawing. Camera: Slow push in on screen, then slight shake conveying frustration. Composition: Extreme close-up of terminal screen with hands at bottom. Focus: Sharp sketch focus on error text and hand movements. Ambiance: Cold blue screen glow sketched with hatching, dark moody atmosphere with heavy shading. Audio: Rapid error beeps, keyboard typing frantically getting louder, frustrated exhale, low piano note begins.""",
            "duration": 8,
            "resolution": "1080p",
            "aspect_ratio": "16:9"
        },

        # Clip 3B: Literature Overwhelm - 8s, 1080p
        {
            "clip_id": "scene_3b_literature_1080p_8s",
            "prompt": """Subject: Person at laptop with many browser tabs and papers. Action: Hands scrolling frantically through papers on screen, head shaking slightly in overwhelm, hand rubbing forehead in stress. Style: Pencil sketch animation, sketchy chaotic lines for papers and tabs, expressive gestural drawing. Camera: Slow push in on overwhelmed face. Composition: Medium shot of person and screen with papers. Focus: Sharp sketch focus on chaos with energetic line work. Ambiance: Cold blue laptop light sketched with hatching, overwhelming atmosphere with heavy shading. Audio: Frantic clicking, rapid scrolling, paper rustling sounds, frustrated breathing.""",
            "duration": 8,
            "resolution": "1080p",
            "aspect_ratio": "16:9"
        },

        # Clip 3C: GPU Queue - 8s, 1080p
        {
            "clip_id": "scene_3c_gpu_queue_1080p_8s",
            "prompt": """Subject: Laptop screen showing queue status with person's face. Action: Cursor hovering then clicking refresh repeatedly, face in reflection showing increasing disappointment, person sighing and head dropping. Style: Pencil sketch animation, clean sketched interface, emotional face drawing. Camera: Static tight close-up, slight drift in showing resignation. Composition: Close-up of screen with face reflection prominent. Focus: Sharp sketch focus on queue text and reflected face. Ambiance: Cold blue screen glow sketched, dark room with deep shadows. Audio: Mouse clicking repeatedly, queue ticking sound, disappointed heavy sigh, clock ticking ominously.""",
            "duration": 8,
            "resolution": "1080p",
            "aspect_ratio": "16:9"
        },

        # Clip 3D: Environment Hell - 8s, 1080p
        {
            "clip_id": "scene_3d_environment_1080p_8s",
            "prompt": """Subject: Hands typing terminal commands with errors. Action: Rapid aggressive typing, errors appearing, typing becoming more frantic, hands suddenly stopping and pulling back in frustration. Style: Pencil sketch animation, bold energetic lines for typing motion, sketchy error text. Camera: Close-up on hands and screen, slight camera shake with frustration. Composition: Close-up of hands and terminal screen. Focus: Sharp sketch focus on typing action and errors. Ambiance: Cold fluorescent lighting sketched with harsh lines. Audio: Keyboard mashing intensifying, error beeps accelerating, frustrated exhale loudly.""",
            "duration": 8,
            "resolution": "1080p",
            "aspect_ratio": "16:9"
        },

        # Clip 3E: Permission Denied - 8s, 1080p
        {
            "clip_id": "scene_3e_permission_denied_1080p_8s",
            "prompt": """Subject: Email inbox with rejection messages. Action: Mouse clicking through emails opening each rejection, scrolling through denials, cursor hovering sadly, person's hand moving to close laptop slowly. Style: Pencil sketch animation, clean sketched UI, emotional hand drawing. Camera: Static close-up with slight slow zoom out showing isolation. Composition: Close-up of screen transitioning to show person's defeated posture. Focus: Sharp sketch focus on rejection text. Ambiance: Cold blue interface light sketched, oppressive atmosphere. Audio: Disappointing notification dings repeating, mouse clicks, heavy defeated sigh, silence building.""",
            "duration": 8,
            "resolution": "1080p",
            "aspect_ratio": "16:9"
        },

        # Clip 3F: Buried in Papers - 8s, 1080p
        {
            "clip_id": "scene_3f_buried_papers_1080p_8s",
            "prompt": """Subject: Person at desk surrounded by tall paper stacks. Action: Person visible initially then camera reveals more papers, final paper stack added obscuring person completely, only hands visible shuffling papers helplessly. Style: Pencil sketch animation, layered sketched paper stacks with texture, expressive overwhelm drawing. Camera: Slow pull back revealing full extent of paper mountains. Composition: Wide shot emphasizing overwhelming paper dominance over person. Focus: Deep sketch focus showing paper stack depth and person buried. Ambiance: Cold fluorescent overhead lighting sketched with harsh shadows, oppressive isolated atmosphere. Audio: Papers rustling heavily, stacks shifting, overwhelming silence underneath, sense of being buried sonically.""",
            "duration": 8,
            "resolution": "1080p",
            "aspect_ratio": "16:9"
        }
    ]

    print("\n🎬 Generating Scene 3 Montage: Infrastructure Hell")
    print(f"   Clips: 3A-3F (6 clips)")
    print(f"   Resolution: 1080p, 16:9")
    print(f"   Duration: 8s per clip")
    print(f"   Style: Pencil sketch animation")
    print()

    generator.generate_sequence(clips)

    print("\n" + "="*60)
    print("🎬 Scene 3 montage clips (3A-3F) generated successfully!")
    print("="*60)


if __name__ == "__main__":
    main()
