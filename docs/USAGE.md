# Usage Guide - Generating Videos with Google Veo 3.1

This guide explains how to use the scripts in this repository to generate your own videos with Google Veo 3.1 API.

---

## Quick Start

### Prerequisites

1. **Google AI API Key**
   - Get one at: https://ai.google.dev/
   - Veo 3.1 access required

2. **Python 3.8+**
   - Required packages in `scripts/core/requirements.txt`

### Installation

```bash
# Navigate to scripts directory
cd scripts/core

# Install dependencies
pip install -r requirements.txt

# Set up API key
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
```

---

## Scripts Overview

### Core Scripts (`scripts/core/`)

These are the **reusable foundation** scripts you'll use for any video generation.

#### `generate_videos.py`

**Purpose:** Main video generation engine

**Features:**
- Generate videos from text prompts
- Support for video extension (continuing from previous clip)
- Rate limiting (60s between requests)
- Resume support (skips already-generated clips)
- Metadata tracking in JSON

**Usage:**
```python
from generate_videos import VeoVideoGenerator

generator = VeoVideoGenerator(api_key="your-api-key")

# Generate a standalone clip
result = generator.generate_clip(
    clip_id="my_clip",
    prompt="Your detailed prompt here...",
    duration=8,              # 4-8 seconds (720p) or 8 only (1080p)
    resolution="1080p",      # "720p" or "1080p"
    aspect_ratio="16:9"
)

# Extend from a previous clip
result = generator.generate_clip(
    clip_id="my_clip_continuation",
    prompt="Continuation prompt...",
    duration=8,
    resolution="720p",       # Must match parent clip resolution
    extend_from_clip="my_clip"
)
```

**Important Notes:**
- 1080p requires 8 second duration
- 720p allows 4-8 seconds
- Extensions must use same resolution as parent clip
- Rate limiting: 60s between requests (configurable)

#### `download_videos.py`

**Purpose:** Download generated videos from Veo URLs

**Usage:**
```bash
python download_videos.py
```

Downloads all videos listed in `../../output/generation_metadata.json` to the `output/` directory.

**Note:** Veo videos expire after 2 days - download promptly!

---

### Experiment Scripts (`scripts/experiments/`)

These scripts show **how we explored** different approaches and styles.

#### `test_styles.py`

Tests 6 different animation styles to find the best aesthetic.

**Styles tested:**
- Watercolor painting animation
- Pencil sketch animation ✅ (winner!)
- Flat vector animation
- Traditional ink wash
- 3D cartoon animation
- Paper cut-out animation

**Usage:**
```bash
cd scripts/experiments
python test_styles.py
```

**Learning:** Pencil sketch style was chosen for its humanistic, hand-crafted feel.

#### `test_single_clip.py`

Minimal test script for validating API setup and basic generation.

#### `test_v5_first_scenes.py`

Early tests of V5 final prompts (pencil sketch with motion).

---

### Production Scripts (`scripts/production/`)

These are **scene-specific** scripts used to generate the actual "Galileo" video clips.

#### `generate_videos_v5_final.py`

**Purpose:** Batch generate all scenes with V5 final prompts

**Usage:**
```bash
cd scripts/production
python generate_videos_v5_final.py
```

Generates all scenes in sequence with appropriate wait times.

#### Individual Scene Scripts

For iterative refinement of specific scenes:

**`generate_scene_1b_discovery_joy.py`**
- Generates Scene 1B (Galileo's eureka moment)
- Extends from Scene 1 (requires Scene 1 at 720p)

**`generate_scene_2_match_cut.py`**
- Generates match cut scene (hand sketching → hand form-filling)
- Extends from Scene 1B

**`generate_scene_3_combined.py`**
- Generates combined montage (split-screen approach)

**`generate_scene_3_montage.py`**
- Generates individual montage clips (terminal, literature, GPU, etc.)

**`generate_scene_6_collective_awakening.py`**
- Generates constellation scene (multiple people emerging)
- Extends from Scene 5

**`regenerate_scene_1_720p.py`**
- Regenerates Scene 1 at 720p for extension compatibility

**Usage:**
```bash
cd scripts/production
python generate_scene_1b_discovery_joy.py
```

---

## Understanding Prompts

All prompt versions are organized in `prompts/`:

### `prompts/v1-initial/`
First attempt - highly detailed, technical, photorealistic

### `prompts/v2-cinematic/`
Simplified, mood-focused, Apple-style aesthetic

### `prompts/v3-refined/`
Balance of specificity and artistic freedom

### `prompts/v4-animated/`
Shift to animated styles (paper cut-out, watercolor, etc.)

### `prompts/v5-final-pencil/` ✅
**Final production prompts** - pencil sketch style with motion

**Use V5 prompts** as your starting point for new generations.

---

## Prompt Structure (Veo Best Practices)

Effective Veo 3.1 prompts include:

1. **Subject:** What/who is in the scene
2. **Action:** What's happening
3. **Style:** Visual aesthetic (e.g., "Pencil sketch animation")
4. **Camera:** Movement, angle, framing
5. **Composition:** Layout, depth of field
6. **Focus:** What's sharp, what's soft
7. **Ambiance:** Lighting, mood, atmosphere
8. **Audio:** Sound cues (optional)

**Example from V5:**
```
Subject: Galileo figure at telescope under starry night sky
Action: Looking through telescope eyepiece, then slowly lifting head upward to gaze at stars with wonder
Style: Pencil sketch animation, hand-drawn loose gestural lines, charcoal shading, expressive artistic sketch aesthetic
Camera: Slow dolly in from wide to medium shot, gentle camera push emphasizing intimacy
Composition: Starting wide shot emphasizing scale - vast cosmos above small figure below, ending medium shot showing face
Focus: Sketch-like focus with hand-drawn quality, stars sketched with radiating lines
Ambiance: Warm golden candlelight from stone villa window mixing with cool blue starlight, intimate night atmosphere
Audio: Gentle night breeze, distant crickets chirping softly, telescope adjusting, breath of wonder, soft contemplative music building
```

---

## Rate Limiting & Quotas

**Default wait time:** 60 seconds between requests

**If you hit rate limits:**

Edit `scripts/core/generate_videos.py`:
```python
WAIT_BETWEEN_REQUESTS = 90  # Increase to 90 seconds
```

**If you hit quota limits:**
- Check usage at: https://ai.dev/usage?tab=rate-limit
- Upgrade plan if needed
- Wait for quota reset

---

## Video Extensions

**What is extension?**
Veo can "continue" a video from its last frame, maintaining visual consistency.

**When to use:**
- Connected narrative scenes (same character, continuous action)
- Camera movements that need continuity
- Scene transitions

**When NOT to use:**
- Distinct locations or moments
- Montage cuts
- Independent scenes

**Requirements:**
- Parent clip must be generated successfully first
- Extension must use **same resolution** as parent
- Extension picks up from last frame automatically

**Example:**
```python
# Generate parent clip
generator.generate_clip(
    clip_id="scene_1",
    prompt="Person looking at stars...",
    resolution="720p"
)

# Extend it
generator.generate_clip(
    clip_id="scene_1b",
    prompt="Same person has eureka moment...",
    resolution="720p",           # Must match!
    extend_from_clip="scene_1"
)
```

---

## Output & Metadata

### Generated Videos

Stored in: `output/`

**Naming convention:**
- Test clips: `test_clip_[name]_[duration]s.mp4`
- Style tests: `test_style_[style]_[duration]s.mp4`
- Production: `scene_[number]_[description]_[resolution]_[duration]s.mp4`

### Metadata

`output/generation_metadata.json` tracks:
- Clip IDs and prompts
- Generation timestamps
- Video URLs and local paths
- Durations and resolutions
- Success/failure status
- Generation time in seconds

**Use this to:**
- Track what's been generated
- Debug failures
- Resume interrupted sessions
- Retrieve video URLs

---

## Troubleshooting

### "GOOGLE_API_KEY not set"
```bash
export GOOGLE_API_KEY="your-api-key"
```
Or add to `scripts/core/.env` file.

### "Resolution 1080p requires duration seconds to be 8"
Change duration to 8 seconds for 1080p:
```python
duration=8,
resolution="1080p"
```

### "Rate limit exceeded"
Increase wait time in `generate_videos.py` or wait for quota reset.

### Extension fails
- Check parent clip was generated successfully
- Verify parent and child use same resolution
- Check `generation_metadata.json` for parent clip data

### "Unknown mime type" for extensions
Update to latest google-generativeai package:
```bash
pip install --upgrade google-generativeai
```

---

## Best Practices

1. **Start with 720p for testing**
   - Faster generation
   - More flexible duration (4-8s)
   - Use for extensions

2. **Test prompts with short clips first**
   - 4s test clips generate faster
   - Iterate on prompt quality

3. **Generate incrementally**
   - Use individual scene scripts
   - Don't batch everything at once
   - Allows for creative adjustments

4. **Monitor generation_metadata.json**
   - Check success/failure status
   - Track generation times
   - Debug issues

5. **Download videos within 2 days**
   - Veo URLs expire
   - Run download_videos.py promptly

6. **Keep backups**
   - Generated videos
   - Metadata JSON
   - Final prompts

---

## Workflow Example

**Goal:** Generate a 3-scene video

```bash
# 1. Setup
cd scripts/core
cp .env.example .env
# Add your API key to .env
pip install -r requirements.txt

# 2. Test your prompt (4s, 720p for speed)
python
>>> from generate_videos import VeoVideoGenerator
>>> gen = VeoVideoGenerator("your-api-key")
>>> gen.generate_clip("test_scene1", "Your prompt...", duration=4, resolution="720p")

# 3. Refine prompt, generate production version
>>> gen.generate_clip("scene1_final", "Refined prompt...", duration=8, resolution="1080p")

# 4. Generate continuation
>>> gen.generate_clip("scene2_final", "Continuation...", duration=8, resolution="1080p", extend_from_clip="scene1_final")

# 5. Download all
cd ..
python download_videos.py

# 6. Review in output/
ls ../../output/
```

---

## Additional Resources

- **Creative Vision:** `docs/creative/video-concept-and-script.md`
- **Evolution Story:** `docs/EVOLUTION.md`
- **Technical Docs:** `docs/technical/`
- **Veo API Docs:** https://ai.google.dev/models/veo

---

**Questions or Issues?**
Check `output/generation_metadata.json` for detailed error messages and generation history.
