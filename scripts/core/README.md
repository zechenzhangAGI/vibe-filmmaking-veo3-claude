# Video Generation Scripts

Python scripts for generating Orchestra launch video using Google Veo 3.1 API.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up API key:**
   ```bash
   export GOOGLE_API_KEY="your_api_key_here"
   ```

   Or create a `.env` file in this directory:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage

### Generate all video clips:

```bash
python generate_videos.py
```

This will:
- Generate all 12 clips in sequence
- Handle rate limiting (60s wait between requests)
- Use extend feature for connected scenes (clips 2, 5, 7)
- Save metadata to `../output/generation_metadata.json`
- Store video URLs for download

### Resume after interruption:

The script automatically skips already-generated clips. Just run again:
```bash
python generate_videos.py
```

## Clip Sequence

| Clip | Duration | Type | Description |
|------|----------|------|-------------|
| 1. Galileo | 5s | Independent | Historical opening |
| 2. Time Collapse | 5s | Extend #1 | 1610→2025 transition |
| 3A. Terminal Errors | 1s | Independent | Debugging hell |
| 3B. Literature Overwhelm | 1s | Independent | Paper overload |
| 3C. GPU Queue | 1s | Independent | Waiting for compute |
| 3D. Environment Hell | 1s | Independent | Setup failures |
| 3E. Permission Denied | 1s | Independent | Grant rejections |
| 3F. Buried in Papers | 1s | Independent | Information buried |
| 4. Breaking Point | 3s | Independent | Giving up moment |
| 5. Light Returns | 4s | Extend #4 | Hope emerges |
| 6. Discovery Abstract | 6s | Independent | Abstract visualization |
| 7. Constellation | 5s | Extend #6 | Community revealed |

**Total: 28 seconds of generated footage**

Text overlays and logo (15s) will be added in post-production.

## Output

Generated clips and metadata saved to:
```
../output/
├── generation_metadata.json  # Clip URLs, timestamps, status
└── [downloaded videos will go here]
```

## Troubleshooting

**Rate limit errors:**
- Increase `WAIT_BETWEEN_REQUESTS` in script
- Default is 60s between requests

**API errors:**
- Check API key is valid
- Verify Veo 3.1 API access enabled
- Check API endpoint URL

**Extend failures:**
- Ensure parent clip generated successfully
- Check parent clip URL is valid
- Generate parent independently if extend fails

## Post-Production Checklist

After generation:

1. ✅ Download all video clips
2. ✅ Review each clip for quality
3. ✅ Create text overlay cards:
   - "1610. Anyone could discover."
   - "2025."
   - Montage text overlays
   - "Science doesn't ask for permission."
   - "It never did."
   - "Return science to the curious."
   - "Orchestra"
4. ✅ Stitch clips in order
5. ✅ Color grade full sequence
6. ✅ Add/adjust audio mix
7. ✅ Final export at 1080p 24fps
