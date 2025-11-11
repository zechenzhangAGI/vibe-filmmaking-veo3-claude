# Quick Start Guide - Orchestra Launch Video Generation

## 🎯 Goal
Generate 42-45 second manifesto-style launch video using Google Veo 3.1 API.

## ⚡ Quick Start (3 Steps)

### 1. Setup (2 minutes)
```bash
cd veo-3-generation/scripts
pip install -r requirements.txt
export GOOGLE_API_KEY="your-api-key"
```

### 2. Generate (12-15 minutes with rate limiting)
```bash
python generate_videos.py
```

This generates 12 clips:
- 1 Galileo opening (5s)
- 1 Time collapse transition (5s)
- 6 Infrastructure hell montage clips (1s each)
- 1 Breaking point (3s)
- 1 Light returns (4s)
- 1 Abstract discovery (6s)
- 1 Constellation pullback (5s)

**Total:** ~28 seconds of generated footage

### 3. Download (5 minutes)
```bash
python download_videos.py
```

## 📝 What Gets Generated

| Act | Clips | Duration | Description |
|-----|-------|----------|-------------|
| **Act I: The Fall** | 8 clips | 18s | Galileo → time collapse → infrastructure hell → breaking point |
| **Act II: The Return** | 3 clips | 15s | Light emerges → abstract discovery → constellation |
| **Act III: Manifesto** | Text overlays (post) | 12s | "Science doesn't ask permission" + logo |

## 🎬 Post-Production Checklist

After generation, you'll need to:

- [ ] Review all 12 clips in `output/` directory
- [ ] Create text overlay cards:
  - [ ] "1610. Anyone could discover."
  - [ ] "2025."
  - [ ] Montage text ("Debugging...", "Reading paper 247...", etc.)
  - [ ] "Science doesn't ask for permission."
  - [ ] "It never did."
  - [ ] "Return science to the curious."
  - [ ] "Orchestra" logo
- [ ] Stitch clips in editing software (Premiere, Final Cut, DaVinci)
- [ ] Color grade full sequence (warm → cold → warm → cream)
- [ ] Audio mix (strings, electronic, silence as power)
- [ ] Export: 1080p, 24fps, 16:9

## 🚨 Troubleshooting

**"GOOGLE_API_KEY not set"**
```bash
export GOOGLE_API_KEY="your-key-here"
```

**Rate limit errors**
- Increase wait time in `generate_videos.py`: `WAIT_BETWEEN_REQUESTS = 90`

**Extend failures**
- Parent clip must be generated successfully first
- Check metadata: `cat ../output/generation_metadata.json`
- Generate parent independently if needed

**Missing clips**
- Script resumes automatically - just run again
- Check generation_metadata.json for status

## 📚 Documentation

- **Full concept:** `video-concept-and-script.md`
- **All prompts:** `veo-prompts.md`
- **Complete README:** `README.md`
- **Scripts docs:** `scripts/README.md`

## ⏱️ Timeline Estimate

| Task | Duration |
|------|----------|
| Setup | 2 min |
| Generate 12 clips | 12-15 min (with 60s waits) |
| Download clips | 5 min |
| **Total automated** | **~20 min** |
| Post-production | 2-4 hours (manual) |

## 🎨 Creative Vision

**Message:** Science was once for anyone with curiosity (Galileo, 1610). It became bureaucratic infrastructure hell (2025). Orchestra returns science to the curious.

**Style:** Apple "Think Different" meets Terrence Malick. Revolutionary, artistic, manifesto-driven. NOT a feature demo.

**Tone:** Sharp, futuristic (scientific Jarvis), but warm and humanistic. Confident, understated ending.

---

**Ready?** Run `python generate_videos.py` and let's create something revolutionary. 🚀
