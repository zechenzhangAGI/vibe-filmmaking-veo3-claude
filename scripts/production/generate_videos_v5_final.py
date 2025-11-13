#!/usr/bin/env python3
"""
Orchestra Launch Video Generator - V5 FINAL
Pencil sketch animation style, 1080p, 8s clips with motion
"""

import os
import time
from dotenv import load_dotenv
from generate_videos import VeoVideoGenerator

load_dotenv()

def main():
    """Generate all clips with V5 final prompts"""

    API_KEY = os.getenv("GOOGLE_API_KEY")
    generator = VeoVideoGenerator(API_KEY)

    # V5 FINAL: Pencil Sketch Style, 1080p, 8s, With Motion
    clips = [
        # Clip 1: Galileo - 8s, 1080p
        {
            "clip_id": "final_clip_1_galileo_8s",
            "prompt": """Subject: Galileo figure at telescope under starry night sky. Action: Looking through telescope eyepiece, then slowly lifting head upward to gaze at stars with wonder, subtle head tilt, contemplative breathing. Style: Pencil sketch animation, hand-drawn loose gestural lines, charcoal shading, expressive artistic sketch aesthetic, visible pencil strokes, animated drawing quality. Camera: Slow dolly in from wide to medium shot, gentle camera push emphasizing intimacy. Composition: Starting wide shot emphasizing scale - vast cosmos above small figure below, ending medium shot showing face. Focus: Sketch-like focus with hand-drawn quality, stars sketched with radiating lines. Ambiance: Warm golden candlelight from stone villa window mixing with cool blue starlight, intimate night atmosphere, sketched light rays. Audio: Gentle night breeze, distant crickets chirping softly, telescope adjusting, breath of wonder, soft contemplative music building.""",
            "duration": 8,
            "resolution": "1080p"
        },

        # Clip 2: Time Collapse - 8s, 1080p, EXTEND from #1
        {
            "clip_id": "final_clip_2_time_collapse_8s",
            "prompt": """Subject: Same telescope scene transforming through time. Action: Rapid time-lapse transformation - sky cycling day/night creating streaking motion, single figure multiplying into crowd, space closing in with walls appearing, equipment morphing. Style: Pencil sketch animation with sketchy time-lapse effect, lines redrawing and transforming, animated sketch metamorphosis. Camera: Locked wide framing throughout transformation, static anchor point emphasizing change. Composition: Same wide shot maintained, transformation happening within frame, sketch lines evolving. Focus: Sketch quality throughout with energetic line work showing transformation. Ambiance: Color temperature shifts from warm golden sketched candlelight to cold blue sketched fluorescent lighting, atmosphere darkening. Audio: Ethereal whooshing time compression sound, organic sounds becoming mechanical, music distorting from classical strings to electronic dissonance.""",
            "duration": 8,
            "resolution": "1080p",
            "extend_from_clip": "final_clip_1_galileo_8s"
        },

        # Clip 3A: Terminal Errors - 8s, 1080p
        {
            "clip_id": "final_clip_3a_terminal_errors_8s",
            "prompt": """Subject: Computer terminal screen with error messages and hands typing. Action: Hands typing frantically, error text scrolling rapidly upward, hands hitting keys harder with frustration, finally hands stopping and pulling back. Style: Pencil sketch animation, bold sketchy lines for text and hands, dynamic gestural drawing. Camera: Slow push in on screen, then slight shake conveying frustration. Composition: Extreme close-up of terminal screen with hands at bottom. Focus: Sharp sketch focus on error text and hand movements. Ambiance: Cold blue screen glow sketched with hatching, dark moody atmosphere with heavy shading. Audio: Rapid error beeps, keyboard typing frantically getting louder, frustrated exhale, low piano note begins.""",
            "duration": 8,
            "resolution": "1080p"
        },

        # Clip 3B: Literature Overwhelm - 8s, 1080p
        {
            "clip_id": "final_clip_3b_literature_8s",
            "prompt": """Subject: Person at laptop with many browser tabs and papers. Action: Hands scrolling frantically through papers on screen, head shaking slightly in overwhelm, hand rubbing forehead in stress. Style: Pencil sketch animation, sketchy chaotic lines for papers and tabs, expressive gestural drawing. Camera: Slow push in on overwhelmed face. Composition: Medium shot of person and screen with papers. Focus: Sharp sketch focus on chaos with energetic line work. Ambiance: Cold blue laptop light sketched with hatching, overwhelming atmosphere with heavy shading. Audio: Frantic clicking, rapid scrolling, paper rustling sounds, frustrated breathing.""",
            "duration": 8,
            "resolution": "1080p"
        },

        # Clip 3C: GPU Queue - 8s, 1080p
        {
            "clip_id": "final_clip_3c_gpu_queue_8s",
            "prompt": """Subject: Laptop screen showing queue status with person's face. Action: Cursor hovering then clicking refresh repeatedly, face in reflection showing increasing disappointment, person sighing and head dropping. Style: Pencil sketch animation, clean sketched interface, emotional face drawing. Camera: Static tight close-up, slight drift in showing resignation. Composition: Close-up of screen with face reflection prominent. Focus: Sharp sketch focus on queue text and reflected face. Ambiance: Cold blue screen glow sketched, dark room with deep shadows. Audio: Mouse clicking repeatedly, queue ticking sound, disappointed heavy sigh, clock ticking ominously.""",
            "duration": 8,
            "resolution": "1080p"
        },

        # Clip 3D: Environment Hell - 8s, 1080p
        {
            "clip_id": "final_clip_3d_environment_8s",
            "prompt": """Subject: Hands typing terminal commands with errors. Action: Rapid aggressive typing, errors appearing, typing becoming more frantic, hands suddenly stopping and pulling back in frustration. Style: Pencil sketch animation, bold energetic lines for typing motion, sketchy error text. Camera: Close-up on hands and screen, slight camera shake with frustration. Composition: Close-up of hands and terminal screen. Focus: Sharp sketch focus on typing action and errors. Ambiance: Cold fluorescent lighting sketched with harsh lines. Audio: Keyboard mashing intensifying, error beeps accelerating, frustrated exhale loudly.""",
            "duration": 8,
            "resolution": "1080p"
        },

        # Clip 3E: Permission Denied - 8s, 1080p
        {
            "clip_id": "final_clip_3e_permission_denied_8s",
            "prompt": """Subject: Email inbox with rejection messages. Action: Mouse clicking through emails opening each rejection, scrolling through denials, cursor hovering sadly, person's hand moving to close laptop slowly. Style: Pencil sketch animation, clean sketched UI, emotional hand drawing. Camera: Static close-up with slight slow zoom out showing isolation. Composition: Close-up of screen transitioning to show person's defeated posture. Focus: Sharp sketch focus on rejection text. Ambiance: Cold blue interface light sketched, oppressive atmosphere. Audio: Disappointing notification dings repeating, mouse clicks, heavy defeated sigh, silence building.""",
            "duration": 8,
            "resolution": "1080p"
        },

        # Clip 3F: Buried in Papers - 8s, 1080p
        {
            "clip_id": "final_clip_3f_buried_papers_8s",
            "prompt": """Subject: Person at desk surrounded by tall paper stacks. Action: Person visible initially then camera reveals more papers, final paper stack added obscuring person completely, only hands visible shuffling papers helplessly. Style: Pencil sketch animation, layered sketched paper stacks with texture, expressive overwhelm drawing. Camera: Slow pull back revealing full extent of paper mountains. Composition: Wide shot emphasizing overwhelming paper dominance over person. Focus: Deep sketch focus showing paper stack depth and person buried. Ambiance: Cold fluorescent overhead lighting sketched with harsh shadows, oppressive isolated atmosphere. Audio: Papers rustling heavily, stacks shifting, overwhelming silence underneath, sense of being buried sonically.""",
            "duration": 8,
            "resolution": "1080p"
        },

        # Clip 4: Breaking Point - 8s, 1080p
        {
            "clip_id": "final_clip_4_breaking_point_8s",
            "prompt": """Subject: Person at desk working. Action: Typing slows then stops completely, hands lift from keyboard, person sits back heavily in chair, looks down at hands turning them over, eyes close slowly, head drops slightly, then fade to pure black screen. Style: Pencil sketch animation, loose emotional gestural lines, charcoal shading showing exhaustion, expressive hand-drawn vulnerability, sketch lines fading to black. Camera: Slow zoom from medium shot to intimate close-up on face showing defeat, smooth continuous push in, then cut to black. Composition: Medium shot transitioning to close-up portrait, ending in darkness. Focus: Shallow sketch focus on face with background fading, emotional pencil work. Ambiance: Harsh overhead lighting sketched with hard lines fading to pure black, darkness consuming the frame. Audio: Typing slowing down, keyboard final key press, chair creaking as lean back, all sound cutting to silence except slow heavy breathing, single heartbeat, then complete powerful silence.""",
            "duration": 8,
            "resolution": "1080p"
        },

        # Clip 5: Light Returns - 8s, 1080p, EXTEND from #4
        {
            "clip_id": "final_clip_5_light_returns_8s",
            "prompt": """Subject: Same person from previous scene. Action: On black screen eyes remain closed, warm light begins emerging from below illuminating face, eyes slowly flutter then open, expression transforms from exhaustion to curiosity to recognition, slight forward lean emerges. Style: Pencil sketch animation, sketchy lines emerging from darkness, warm light drawn with soft flowing lines, emotional transformation visible in loose expressive drawing. Camera: Intimate close-up on face, slight slow push in as eyes open emphasizing recognition moment. Composition: Close-up portrait, face emerging from darkness into warm light. Focus: Shallow sketch focus on eyes and face, warm light sketched with soft radiating lines. Ambiance: Pure black transforming to warm golden amber light from below like Caravaggio, hope sketched with luminous quality, light painted with warm flowing strokes. Audio: Soft electronic hum, breath becoming lighter and hopeful, single pure piano note ringing clear, warm ambient pad with strings begins underneath building gently.""",
            "duration": 8,
            "resolution": "1080p",
            "extend_from_clip": "final_clip_4_breaking_point_8s"
        },

        # Clip 6: Discovery Abstract - 8s, 1080p
        {
            "clip_id": "final_clip_6_discovery_abstract_8s",
            "prompt": """Subject: Abstract visualization of ideas and discovery. Action: Blue ink dispersing and flowing organically in water creating spreading patterns, neural network nodes lighting up in sequence like connections firing, equations appearing and linking together with animated connecting lines, data streams flowing like rivers with current motion, light refracting through prisms creating moving spectrum. Style: Abstract pencil sketch animation, flowing organic sketch lines, warm blue and amber gold hand-drawn aesthetic, painterly sketched quality with visible strokes, animated artistic interpretation. Camera: Floating camera moving fluidly through abstract sketch space, gentle organic camera flow following ink dispersal. Composition: Abstract composition with no traditional framing, flowing visual poetry. Focus: Soft atmospheric sketch focus with glowing elements, dreamlike pencil quality. Ambiance: Warm blue and amber gold tones sketched with flowing lines, luminous and alive with organic flowing energy, hand-drawn warmth. Audio: Warm electronic ambient music building, water flowing sounds, gentle harmonics, soft electronic pulses, hopeful restrained strings swelling, organic sounds mixed with digital.""",
            "duration": 8,
            "resolution": "1080p"
        },

        # Clip 7: Constellation - 8s, 1080p, EXTEND from #6
        {
            "clip_id": "final_clip_7_constellation_8s",
            "prompt": """Subject: Multiple people at laptops in different locations connected by warm light. Action: Camera pulls back from abstract visuals revealing person working at laptop, camera continues pulling back steadily, more people appear scattered in darkness each illuminated by laptop glow, people typing and working with subtle movements, constellation pattern emerging. Style: Pencil sketch animation, soft sketched style with warm glowing lights drawn with radiating lines, contemplative artistic aesthetic, hand-drawn human warmth. Camera: Slow steady pull back from abstract close-up to wide reveal, smooth continuous backward dolly movement. Composition: Wide shot revealing constellation pattern of scattered people, visual metaphor of lights in darkness. Focus: Soft sketch focus creating warm atmosphere, glowing laptop lights emphasized with sketched radiance. Ambiance: Warm laptop screen glows sketched in darkness like stars with soft halos, constellation pattern, intimate and connected atmosphere with hand-drawn warmth. Audio: Multiple keyboards typing rhythmically creating musical pattern, warm strings swelling emotionally but remaining restrained, collective breathing sounds, sense of community building, connection emphasized.""",
            "duration": 8,
            "resolution": "1080p",
            "extend_from_clip": "final_clip_6_discovery_abstract_8s"
        }
    ]

    # Generate all clips in sequence
    print("\n🎬 Generating V5 FINAL: Pencil Sketch Style @ 1080p")
    print(f"   Total clips: {len(clips)}")
    print(f"   Resolution: 1080p, 16:9")
    print(f"   Duration: 8s per clip")
    print(f"   Style: Pencil sketch animation with motion")
    print()

    generator.generate_sequence(clips)

    print("\n" + "="*60)
    print("🎬 All V5 final clips generated successfully!")
    print("="*60)


if __name__ == "__main__":
    main()
