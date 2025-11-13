# The Evolution of "Galileo" - Orchestra Launch Video

This document chronicles the creative and technical journey of generating Orchestra's launch video using Google Veo 3.1 API.

## Overview

**Goal:** Create a 42-45 second manifesto-style launch video that tells the story of science returning to the curious.

**Final Result:** "Galileo" - A pencil sketch animated video showing the journey from Galileo's wonder (1610) through modern bureaucratic infrastructure hell, to Orchestra's vision of democratized science.

---

## Creative Evolution

### Version 1: Initial Detailed Prompts (v1-initial)
**Date:** Early November 2024
**Location:** `prompts/v1-initial/veo-prompts.md`

**Approach:**
- Highly detailed, technical prompts
- Specific camera movements, lens specs, film stock
- Literal descriptions of every element
- Photorealistic aesthetic

**Example:**
> "Galileo Galilei stands at a brass telescope gazing upward at infinite starry night sky in 1610 Tuscany. Wide cinematic establishing shot emphasizing dramatic scale of cosmos above and single human figure below. Period-accurate Renaissance clothing, doublet and robe..."

**Learning:** Too literal, prompts were overly prescriptive

---

### Version 2: Cinematic Apple-Style (v2-cinematic)
**Location:** `prompts/v2-cinematic/veo-prompts-v2-cinematic.md`

**Approach:**
- Simplified prompts focusing on mood and emotion
- Apple "Think Different" aesthetic inspiration
- Less technical detail, more artistic interpretation
- Still photorealistic

**Example:**
> "Cinematic wide shot of a lone figure at telescope under infinite starry sky. Dramatic scale - vast cosmos above, single silhouette below. Warm golden light from window contrasts with cool blue starlight. Face tilted upward in pure wonder."

**Learning:** Better mood, but still too realistic and literal

---

### Version 3: Refined Balance (v3-refined)
**Location:** `prompts/v3-refined/veo-prompts-v3-refined.md`

**Approach:**
- Balance between specificity and artistic freedom
- Kept key details (Galileo, settings) but simplified language
- More cinematic language while maintaining narrative clarity
- Terrence Malick aesthetic inspiration
- Still photorealistic

**Learning:** Good narrative flow, but photorealism felt too literal for manifesto message

---

### Version 4: Animated Exploration (v4-animated)
**Location:** `prompts/v4-animated/veo-prompts-v4-animated.md`

**Approach:**
- **Major shift:** Explored animated/illustrated styles
- Tested: paper cut-out, watercolor, pencil sketch, vector, ink wash, 3D cartoon
- Apple-ad aesthetic through animation rather than live-action
- Better taste, more artistic

**Key Experiments:**
- Paper cut-out animation with layered depth
- Watercolor painting animation with soft brushstrokes
- **Pencil sketch animation** (winner!) with hand-drawn gestural lines
- Flat vector animation (Kurzgesagt-style)
- Traditional Chinese ink wash
- 3D cartoon (Pixar-inspired)

**Learning:** Pencil sketch style won - artistic, expressive, humanistic but not literal

---

### Version 5: Final Production (v5-final-pencil) ✅
**Location:** `prompts/v5-final-pencil/veo-prompts-v5-final-pencil.md`

**Approach:**
- **Style locked:** Pencil sketch animation throughout
- **Production specs:** 1080p, 8s clips, 16:9 aspect ratio
- **Added motion:** Camera movements, character actions, emotional beats
- **Refined narrative:** Added Scene 1B (Galileo's eureka moment + sketching)
- **Match cut technique:** Hand sketching → hand form-filling (discovery → bureaucracy)

**Key Scenes:**
1. **Scene 1:** Galileo looking through telescope, lifting head in wonder
2. **Scene 1B (NEW):** Galileo's eureka moment - sees Jupiter's moons, sketches discovery with joy
3. **Scene 2:** Match cut - hand sketching → modern researcher filling forms (bureaucracy)
4. **Scene 3:** Infrastructure hell montage (terminal errors, GPU queues, papers, etc.)
5. **Scene 4:** Breaking point - defeat and darkness
6. **Scene 5:** Light returns - warm glow from laptop, hope emerges
7. **Scene 6:** Collective awakening - constellation of curious people

**Why This Worked:**
- Pencil sketch = humanistic, artistic, not corporate
- Motion added life and emotional impact
- Match cut powerfully contrasts joy of discovery vs. bureaucratic drudgery
- Consistent aesthetic throughout all scenes

---

## Technical Evolution

### Early Experiments (`scripts/experiments/`)

**test_single_clip.py**
- First API integration test
- Tested basic Veo 3.1 generation
- Learned: 720p = 4-8s, 1080p = 8s only

**test_styles.py**
- Systematic style testing
- Generated 6 different animation styles
- Clips: watercolor, pencil, vector, ink, 3D cartoon, paper cut-out
- **Result:** Pencil sketch chosen as final style

**test_two_more.py, test_v5_first_scenes.py**
- Early V5 prompt testing
- Validated pencil sketch aesthetic
- Tested camera motion and character actions

### Core Engine (`scripts/core/`)

**generate_videos.py**
- Main reusable video generation engine
- Handles: rate limiting, resume support, metadata tracking, extension
- Used by all production scripts

**download_videos.py**
- Downloads generated videos from Veo URLs
- Manages local file storage

**requirements.txt**
- Python dependencies: google-generativeai, python-dotenv

### Production Scripts (`scripts/production/`)

**generate_videos_v5_final.py**
- Batch generation with all V5 final prompts
- Sequential generation of all scenes

**generate_scene_*.py**
- Individual scene generators for iterative refinement
- `generate_scene_1b_discovery_joy.py` - Added eureka moment
- `generate_scene_2_match_cut.py` - Match cut scene with extension
- `generate_scene_3_combined.py` - Combined montage approach
- `generate_scene_3_montage.py` - Individual montage clips
- `generate_scene_6_collective_awakening.py` - Constellation scene

**regenerate_scene_1_720p.py**
- Re-generated Scene 1 at 720p for extension compatibility
- Learned: Extensions require same resolution as parent clip

---

## Key Learnings

### Creative Insights

1. **Animation > Photorealism for Manifestos**
   - Animated styles feel more artistic, less corporate
   - Pencil sketch = humanistic, hand-crafted, authentic

2. **Less is More in Prompts**
   - V1 was too prescriptive, V2-V5 progressively simplified
   - Focus on mood, emotion, and key visual elements

3. **Match Cuts Are Powerful**
   - Hand sketching → hand form-filling shows transformation viscerally
   - Same gesture, opposite meaning = powerful contrast

4. **Motion Adds Life**
   - Static poses felt flat
   - Camera movement + character action = emotional engagement

### Technical Insights

1. **Resolution = Duration Constraint**
   - 720p: 4-8 seconds
   - 1080p: 8 seconds only
   - Extensions require matching resolution

2. **Rate Limiting Matters**
   - 60 second waits between requests
   - Quota limits hit during heavy generation

3. **Iterative Refinement**
   - Individual scene scripts allowed rapid iteration
   - Resume support crucial for long generation sessions

4. **Style Consistency**
   - Keeping pencil sketch throughout all scenes = cohesive aesthetic
   - Veo maintains style well with consistent prompting

---

## Timeline

**November 11, 2024:**
- Initial setup and testing (V1-V3 prompts)
- Style experiments (6 different animation styles)
- V5 first tests (Galileo, terminal errors, breaking point)
- Scene 1 at 720p generated
- **Pencil sketch style selected**

**November 12, 2024:**
- Scene 1B (discovery joy) added to narrative
- Scene 2 (match cut) generated with extension
- Scene 3 montage (6 variations generated)
- Individual montage clips (3a-3f) at 1080p
- Scene 6 (collective awakening) extended from Scene 5
- Production pipeline complete

---

## What Was Generated

### Test Clips (720p, 4s)
- `test_clip_galileo_4s` - V1 prompt
- `test_clip_galileo_v3_4s` - V3 refined
- `test_clip_4_breaking_point_4s` - Defeat moment
- `test_clip_6_abstract_6s` - Abstract discovery
- `test_clip_galileo_v4_animated_4s` - V4 paper cut-out
- Style tests: watercolor, pencil, vector, ink, 3D cartoon (6 clips)

### Production Clips (V5 Final, 1080p, 8s)
- `v5_test_clip_1_galileo_8s` - Final Galileo with motion
- `v5_test_clip_3a_terminal_8s` - Terminal errors
- `v5_test_clip_4_breaking_8s` - Breaking point final
- `scene_1_galileo_720p_8s` - Scene 1 at 720p for extension
- `scene_1b_720p` - Discovery joy (extended from Scene 1)
- `scene_2_match_cut_720p_8s` - Bureaucracy match cut
- `scene_3_combined_montage_1080p_8s` - Combined montage
- `scene_3a-3f_1080p_8s` - Individual montage clips (6 clips)
- `scene_5_light_720p` - Light returns
- `scene_6_collective_awakening_720p_8s` - Constellation

**Total Generated:** 26 video clips across all versions

---

## Files Generated

### Videos
- 26 MP4 files in `output/`
- Mix of tests (720p, 4s) and production (1080p, 8s)
- Total size: ~850MB

### Metadata
- `output/generation_metadata.json` - Complete generation log
- Tracks: prompts, durations, resolutions, timestamps, errors
- 511 lines of generation history

### Support Files
- Last frame PNGs for extensions
- Test style variations in subdirectory

---

## Next Steps (Post-Production)

The generated clips are **raw footage**. Post-production needs:

1. **Editing:**
   - Stitch clips in sequence
   - Speed up/slow down as needed
   - Cut to 42-45 seconds total

2. **Text Overlays:**
   - "1610. Anyone could discover."
   - "2025."
   - Montage text ("Debugging...", etc.)
   - Manifesto statements
   - Orchestra logo

3. **Color Grading:**
   - Warm → cold → warm → cream journey
   - Consistent pencil sketch aesthetic

4. **Audio:**
   - Custom music score (strings, electronic, silence)
   - Sound design (match prompts)
   - Mix to final

5. **Export:**
   - 1080p, 24fps, 16:9
   - Deliver as "Galileo"

---

## Conclusion

What started as detailed photorealistic prompts evolved into artistic pencil sketch animation. The journey taught us that **manifestos need art, not realism** - and that iterative experimentation leads to better creative outcomes.

The "Galileo" video is not just a product demo. It's a statement about returning science to the curious, told through the evolution of visual storytelling itself.

---

*This evolution is preserved in this repository as a record of the creative process.*
