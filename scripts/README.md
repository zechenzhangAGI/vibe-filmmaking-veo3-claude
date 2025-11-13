# Scripts Directory

All Python scripts for generating videos with Google Veo 3.1 API, organized by purpose.

## Directory Structure

```
scripts/
├── core/                # Reusable generation engine
├── experiments/         # Style and approach testing
└── production/          # Final scene generators
```

## Quick Navigation

### Core Scripts (`core/`)

**Start here** for generating your own videos:

- **generate_videos.py** - Main video generation engine (reusable)
- **download_videos.py** - Download generated videos
- **requirements.txt** - Python dependencies
- **.env.example** - API key template
- **README.md** - Core scripts documentation
- **SETUP.md** - Setup instructions

### Experiments (`experiments/`)

**Explore** different styles and approaches:

- **test_styles.py** - Test 6 animation styles (watercolor, pencil, vector, ink, 3D, paper cut-out)
- **test_single_clip.py** - Basic API validation
- **test_two_more.py** - Early experiments
- **test_v5_first_scenes.py** - V5 prompt validation

### Production (`production/`)

**Scene-specific** generators for the "Galileo" video:

- **generate_videos_v5_final.py** - Batch generate all scenes
- **generate_scene_1b_discovery_joy.py** - Galileo eureka moment
- **generate_scene_2_match_cut.py** - Bureaucracy transition
- **generate_scene_3_combined.py** - Montage combined
- **generate_scene_3_montage.py** - Montage individual clips
- **generate_scene_6_collective_awakening.py** - Constellation scene
- **regenerate_scene_1_720p.py** - Resolution adjustment

## Getting Started

```bash
# Setup
cd core
pip install -r requirements.txt
cp .env.example .env
# Add your GOOGLE_API_KEY to .env

# Generate your first video
python
>>> from generate_videos import VeoVideoGenerator
>>> gen = VeoVideoGenerator(api_key="your-key")
>>> gen.generate_clip("test", "Your prompt...", duration=8, resolution="1080p")
```

## Documentation

- **Core usage:** `core/README.md` and `core/SETUP.md`
- **Complete guide:** `../docs/USAGE.md`
- **Evolution story:** `../docs/EVOLUTION.md`

## Import Path Note

When importing from subdirectories, adjust your Python path:

```python
# From experiments/ or production/
import sys
sys.path.append('../core')
from generate_videos import VeoVideoGenerator
```

Or run from the parent directory:
```bash
cd scripts
python -c "from core.generate_videos import VeoVideoGenerator; ..."
```
