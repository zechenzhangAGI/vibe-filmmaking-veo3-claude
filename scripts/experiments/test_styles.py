#!/usr/bin/env python3
"""
Test different animation styles for the Galileo opening scene
"""

import os
import sys
from dotenv import load_dotenv
from generate_videos import VeoVideoGenerator

load_dotenv()

def main():
    """Generate multiple style tests"""

    print("🎨 Orchestra Launch Video - Style Tests")
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

    # Test different styles
    styles = [
        {
            "name": "Watercolor Painting",
            "clip_id": "test_style_watercolor_4s",
            "prompt": """Subject: Galileo figure at telescope under starry night sky. Action: Gazing upward at stars, static contemplative pose. Style: Watercolor painting animation, soft flowing brushstrokes, painted texture, artistic hand-painted aesthetic, gentle color bleeding. Camera: Static wide shot. Composition: Wide shot emphasizing scale - vast cosmos above, small figure below. Focus: Soft focus with watercolor texture. Ambiance: Warm golden candlelight from window mixing with cool blue starlight, intimate night atmosphere, painted luminous quality. Audio: Gentle night breeze, distant crickets chirping softly, soft contemplative music."""
        },
        {
            "name": "Pencil Sketch",
            "clip_id": "test_style_pencil_4s",
            "prompt": """Subject: Galileo figure at telescope under starry night sky. Action: Gazing upward at stars, static contemplative pose. Style: Pencil sketch animation, hand-drawn loose gestural lines, charcoal shading, expressive artistic sketch aesthetic, visible pencil strokes. Camera: Static wide shot. Composition: Wide shot emphasizing scale - vast cosmos above, small figure below. Focus: Sketch-like focus with hand-drawn quality. Ambiance: Warm golden candlelight from window mixing with cool blue starlight, intimate night atmosphere, sketched lighting. Audio: Gentle night breeze, distant crickets chirping softly, soft contemplative music."""
        },
        {
            "name": "Flat Vector Animation",
            "clip_id": "test_style_vector_4s",
            "prompt": """Subject: Galileo figure at telescope under starry night sky. Action: Gazing upward at stars, static contemplative pose. Style: Flat vector animation, clean geometric shapes, modern minimalist design, smooth gradients, Kurzgesagt-inspired aesthetic. Camera: Static wide shot. Composition: Wide shot emphasizing scale - vast cosmos above, small figure below. Focus: Sharp clean vector focus. Ambiance: Warm golden candlelight from window mixing with cool blue starlight, intimate night atmosphere, flat design lighting. Audio: Gentle night breeze, distant crickets chirping softly, soft contemplative music."""
        },
        {
            "name": "Ink Wash Painting",
            "clip_id": "test_style_ink_4s",
            "prompt": """Subject: Galileo figure at telescope under starry night sky. Action: Gazing upward at stars, static contemplative pose. Style: Traditional Chinese ink wash painting animation, flowing black ink, delicate brushwork, minimalist Eastern aesthetic, atmospheric gradients. Camera: Static wide shot. Composition: Wide shot emphasizing scale - vast cosmos above, small figure below. Focus: Soft atmospheric focus with ink wash quality. Ambiance: Warm golden candlelight from window mixing with cool blue starlight, intimate night atmosphere, misty ink wash atmosphere. Audio: Gentle night breeze, distant crickets chirping softly, soft contemplative music."""
        },
        {
            "name": "3D Cartoon",
            "clip_id": "test_style_3d_cartoon_4s",
            "prompt": """Subject: Galileo figure at telescope under starry night sky. Action: Gazing upward at stars, static contemplative pose. Style: 3D cartoon animation, Pixar-inspired aesthetic, soft lighting, appealing character design, warm stylized rendering. Camera: Static wide shot. Composition: Wide shot emphasizing scale - vast cosmos above, small figure below. Focus: Cinematic 3D focus with depth of field. Ambiance: Warm golden candlelight from window mixing with cool blue starlight, intimate night atmosphere, cinematic 3D lighting. Audio: Gentle night breeze, distant crickets chirping softly, soft contemplative music."""
        }
    ]

    for i, style in enumerate(styles, 1):
        print(f"\n{'='*60}")
        print(f"📹 Test {i}/{len(styles)}: {style['name']}")
        print(f"{'='*60}\n")

        try:
            result = generator.generate_clip(
                clip_id=style['clip_id'],
                prompt=style['prompt'],
                duration=4,
                resolution="720p",
                aspect_ratio="16:9"
            )
            print(f"✅ {style['name']} generated: {result['video_path']}")
            print()
        except Exception as e:
            print(f"❌ {style['name']} failed: {e}")
            print()

    print("="*60)
    print("🎨 All style tests complete!")
    print()
    print("Generated styles:")
    for i, style in enumerate(styles, 1):
        print(f"{i}. {style['name']}")
    print()
    print("Compare all versions to choose the best artistic direction!")
    print("="*60)

if __name__ == "__main__":
    main()
