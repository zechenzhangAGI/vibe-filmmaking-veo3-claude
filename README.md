# Veo 3.1 Video Generation - Orchestra Launch Video

## Overview

This directory contains all prompts and scripts for generating the 42-45 second Orchestra launch video "Return Science to the Curious" using Google's Veo 3.1 API.

## Production Strategy

Based on Veo 3.1 capabilities:
- **Max duration:** 8 seconds per clip at 1080p, 24fps
- **Video extension:** Use extend feature for connected narrative scenes
- **Audio:** Native audio generation with video

### Workflow:

1. **Generate clips** using Veo 3.1 with detailed prompts
2. **Use extend** for clips 2, 5, and 7 (connected to previous clip)
3. **Generate independently** for other clips (montage, distinct moments)
4. **Post-production:** stitch, add text overlays, final color grade

## Video Structure

Total duration: 42-45 seconds
Breakdown into manageable Veo clips (8s max each):

| Segment | Time | Clips | Description |
|---------|------|-------|-------------|
| **Act I: Galileo's Wonder** | 0-5s | 1 clip (5s) | Historical opening |
| **Act I: Time Collapse** | 5-10s | 1 clip (5s) | Transition to modern |
| **Act I: Infrastructure Hell** | 10-15s | 2 clips (6x1s cuts) | Montage - generate separately |
| **Act I: Breaking Point** | 15-18s | 1 clip (3s) | Defeat moment |
| **Act II: Light Returns** | 18-22s | 1 clip (4s) | Hope emerges |
| **Act II: Discovery Abstract** | 22-28s | 1 clip (6s) | Abstract visuals |
| **Act II: Constellation** | 28-33s | 1 clip (5s) | Global connection |
| **Act III: Manifesto** | 33-38s | Text overlay (no generation) | Typography |
| **Act III: Call** | 38-42s | Text overlay (no generation) | Typography |
| **Act III: Logo** | 42-45s | Static frame (no generation) | Logo hold |

**Total clips to generate:** ~8-10 video clips

## Directory Structure

```
veo-3-generation/
├── README.md (this file)
├── video-concept-and-script.md (complete creative brief)
├── veo-prompts.md (detailed Veo 3.1 prompts for each scene)
├── scripts/
│   ├── generate_videos.py (Veo 3.1 video generation with extend)
│   ├── download_videos.py (Download generated clips)
│   ├── requirements.txt (Python dependencies)
│   └── README.md (Scripts documentation)
└── output/
    ├── generation_metadata.json (clip URLs, status, timestamps)
    └── [downloaded video clips]
```

## Veo 3.1 Prompt Structure

Based on Google's documentation, effective prompts include:

1. **Subject:** What/who is in the scene
2. **Action:** What's happening
3. **Style:** Visual aesthetic, period, tone
4. **Camera:** Position, movement, lens
5. **Composition:** Framing, depth of field
6. **Focus/Lens:** What's sharp, what's bokeh
7. **Ambiance:** Lighting, mood, atmosphere
8. **Audio:** Dialogue, sound effects, music (optional)

### Example Template:
```
[SUBJECT] [ACTION] in [SETTING]. [STYLE] cinematography.
[CAMERA MOVEMENT] from [ANGLE]. [COMPOSITION] with [FOCUS].
[LIGHTING] creating [AMBIANCE]. [AUDIO CUE].
Shot on [CAMERA/FILM]. [MOOD].
```

## Setup

1. **Navigate to scripts directory:**
```bash
cd veo-3-generation/scripts
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set API key:**
```bash
export GOOGLE_API_KEY="your-google-api-key"
```

## Usage

### Step 1: Generate All Video Clips
```bash
python generate_videos.py
```

This will:
- Generate all 12 clips in sequence (1 Galileo + 1 Time Collapse + 6 Hell Montage + 1 Breaking Point + 1 Light Returns + 1 Discovery + 1 Constellation)
- Use extend feature for clips 2, 5, and 7
- Wait 60 seconds between requests to avoid rate limits
- Save metadata to `output/generation_metadata.json`

### Step 2: Download Generated Videos
```bash
python download_videos.py
```

Downloads all clips from URLs to `output/` directory.

### Step 3: Post-Production
1. Review clips in `output/` directory
2. Create text overlay cards for manifesto statements
3. Stitch clips in video editing software
4. Add final color grading and audio mixing
5. Export final 42-45s video at 1080p 24fps

## Technical Specs

- **Resolution:** 1080p (recommended for final quality)
- **Frame Rate:** 24fps (cinematic)
- **Aspect Ratio:** 16:9
- **Duration per clip:** 3-8 seconds
- **Format:** Video generation returns URLs (download within 2 days)

## Important Notes

- **Rate Limits:** 60s wait between requests (configurable in script)
- **Generation Time:** 11 seconds to 6 minutes per clip
- **Video Retention:** Download within 2 days of generation
- **Watermarks:** Veo 3.1 may add watermarks to generated content
- **Model:** Using `veo-3.1-generate-preview` for best quality
- **Resume Support:** Script automatically skips already-generated clips

## Clip Generation Strategy

| Clip | Type | Reasoning |
|------|------|-----------|
| 1. Galileo | Independent | Opening shot, no prior context |
| 2. Time Collapse | **Extend from #1** | Same framing, continuous transition |
| 3A-3F. Hell Montage | Independent (each) | Rapid cuts, distinct locations |
| 4. Breaking Point | Independent | Distinct emotional beat |
| 5. Light Returns | **Extend from #4** | Same person, lighting change |
| 6. Discovery Abstract | Independent | Abstract visuals, different style |
| 7. Constellation | **Extend from #6** | Pull back from abstract to concrete |

## Files Reference

- **`video-concept-and-script.md`**: Complete creative brief, emotional arcs, visual language
- **`veo-prompts.md`**: Detailed Veo 3.1 prompts with technical specs for each clip
- **`scripts/generate_videos.py`**: Main generation script with rate limiting and extend support
- **`scripts/download_videos.py`**: Download helper for generated clips
- **`output/generation_metadata.json`**: Generated clip URLs, timestamps, and status
