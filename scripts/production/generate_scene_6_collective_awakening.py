#!/usr/bin/env python3
"""
Generate Scene 6: Collective Awakening
Extends from 5_light.mp4 (already 720p)
Multiple people emerging from darkness, opening eyes
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from generate_videos import VeoVideoGenerator

load_dotenv()

def main():
    """Generate Scene 6 Collective Awakening extending from Scene 5"""

    print("🎬 Generating Scene 6: Collective Awakening")
    print("   Extends from: 5_light.mp4")
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

    # Check if 5_light.mp4 exists
    output_dir = Path(__file__).parent.parent / "output"
    scene_5_path = output_dir / "5_light.mp4"

    if not scene_5_path.exists():
        print("❌ Error: 5_light.mp4 not found!")
        print(f"   Expected at: {scene_5_path}")
        sys.exit(1)

    print(f"✅ Found Scene 5: {scene_5_path.name}")

    # Add it to metadata if not already there
    if "scene_5_light_720p" not in generator.metadata.get("clips", {}):
        print("📝 Adding scene_5_light_720p to metadata...")
        generator.metadata["clips"]["scene_5_light_720p"] = {
            "clip_id": "scene_5_light_720p",
            "video_path": str(scene_5_path),
            "video_filename": "5_light.mp4",
            "resolution": "720p",
            "duration": 8,
            "aspect_ratio": "16:9"
        }
        generator._save_metadata()
        print("✅ Metadata updated")

    print()

    # Scene 6: Collective Awakening - EXTENDS from Scene 5
    print("📹 Scene 6: Collective Awakening")
    print("   Multiple people emerging from darkness")
    print("   Intimate close-ups of faces opening eyes")
    print("   Building collective hope and movement")
    print()

    prompt = """Subject: Same person from previous scene with additional people emerging alongside in darkness
Action: Continuing from previous scene, original person's face now fully illuminated by warm golden amber light from below with eyes open showing recognition and slight forward lean, camera holds on this person maintaining same intimate close-up framing. As camera stays on original person, warm lights begin glowing in darkness to the left and right sides - more faces emerging from black background alongside the original person. Second face appears in darkness to left with warm light beginning to glow from below illuminating features, eyes closed then slowly flutter open with hope. Third face emerges to right in darkness with warm light growing from below, eyes opening with curiosity. Fourth and fifth faces appear further in background darkness on both sides, each with their own warm light from below beginning to illuminate, eyes opening one by one. All faces remain in frame together - original person centered in foreground still lit, new people emerging in darkness around them at different depths creating sense of community forming. Original person stays constant anchor while others join the awakening around them in same darkness and warm light aesthetic.
Style: Pencil sketch animation, sketchy lines emerging from darkness exactly matching Scene 5 style, warm light drawn with soft flowing lines illuminating each face from below, emotional transformation visible in loose expressive drawing, charcoal darkness surrounding all figures, same hand-drawn aesthetic maintained throughout
Camera: Intimate close-up on original person's face maintained from previous scene, slight slow pull back revealing more space as additional faces emerge in darkness around them, gentle camera movement emphasizing community forming while keeping original person as anchor
Composition: Close-up portrait of original person centered in foreground, additional faces appearing in darkness at different depths around them creating layered composition, faces emerging from pure black into warm light
Focus: Shallow sketch focus on faces with warm light sketched with soft radiating lines, background darkness remains deep black with heavy charcoal, same luminous quality from Scene 5 maintained
Ambiance: Pure black transforming to multiple warm golden amber lights from below like Caravaggio, hope sketched with luminous quality exactly matching Scene 5, light painted with warm flowing strokes, multiple points of warm light emerging in darkness creating constellation of hope
Audio: Soft electronic hum continues, breath becoming lighter and hopeful with additional breathing sounds layering as more people emerge, piano notes building, warm ambient pad with strings swelling gently, sense of collective awakening building, movement forming"""

    try:
        result = generator.generate_clip(
            clip_id="scene_6_collective_awakening_720p_8s",
            prompt=prompt,
            duration=8,
            resolution="720p",
            aspect_ratio="16:9",
            extend_from_clip="scene_5_light_720p"
        )

        print()
        print("="*60)
        print("🎉 SUCCESS! Scene 6 generated!")
        print("="*60)
        print()
        print(f"📋 Clip Details:")
        print(f"   ID: {result['clip_id']}")
        print(f"   Extended from: Scene 5 (Light Returns)")
        print(f"   Video Path: {result['video_path']}")
        print(f"   Generation Time: {result.get('generation_time_seconds', 'N/A')}s")
        print()
        print("📝 What this shows:")
        print("   - Multiple people emerging from darkness")
        print("   - Each person lifting head and opening eyes")
        print("   - Diverse faces: elderly, young, teenager, parent, researcher")
        print("   - Building from individual to collective awakening")
        print("   - Warm light illuminating faces one by one")
        print("   - Intimate human moments of hope emerging")
        print()
        print("🎬 Next step:")
        print("   Review Scene 6 collective awakening")
        print("   Ready for final manifesto text overlay")
        print("="*60)

    except Exception as e:
        print()
        print("="*60)
        print("❌ FAILED to generate Scene 6")
        print("="*60)
        print()
        print(f"Error: {str(e)}")
        print()
        print("Troubleshooting:")
        print("1. Make sure Scene 5 was added to metadata")
        print("2. Check that the video file exists")
        print("3. Verify API key and connection")
        sys.exit(1)

if __name__ == "__main__":
    main()
