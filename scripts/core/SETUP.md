# Setup Guide

## Quick Setup (3 steps)

### 1. Install Dependencies
```bash
cd veo-3-generation/scripts
pip install -r requirements.txt
```

### 2. Add Your API Key
Open `scripts/.env` and add your Google API key:
```bash
GOOGLE_API_KEY=your_actual_api_key_here
```

### 3. Test with Single Clip
```bash
python test_single_clip.py
```

This will:
- ✅ Verify API key is loaded
- ✅ Test connection to Veo 3.1 API
- ✅ Generate a 3-second test clip (Galileo scene)
- ✅ Save to `output/generation_metadata.json`

**Expected time:** 10 seconds to 6 minutes

## If Test Succeeds ✅

Run full generation:
```bash
python generate_videos.py
```

This generates all 12 clips (~20 minutes with rate limiting)

## If Test Fails ❌

### Error: "GOOGLE_API_KEY not found"
- Open `scripts/.env`
- Make sure it contains: `GOOGLE_API_KEY=your_key`
- No quotes, no spaces around `=`

### Error: API authentication failed
- Check API key is correct
- Verify Veo 3.1 API access enabled in Google Cloud Console
- Ensure billing is set up

### Error: Model not found
- Verify using `veo-3.1-generate-preview` model
- Check API endpoint: `https://generativelanguage.googleapis.com/v1beta/models/veo-3.1-generate-preview:generateVideo`

### Error: Rate limit exceeded
- Wait 60 seconds and try again
- Veo 3.1 has request limits per minute

## Environment File Structure

**`.env`** (your actual keys - NOT committed to git):
```
GOOGLE_API_KEY=AIzaSyB...your_actual_key...xyz123
```

**`.env.example`** (template - safe to commit):
```
GOOGLE_API_KEY=your_google_api_key_here
```

## Security Notes

⚠️ **NEVER commit `.env` to git** - it contains your API key!
- `.gitignore` is configured to protect `.env`
- Only `.env.example` is tracked by git
- Keep your API key private

## Next Steps

After successful test:
1. Generate all clips: `python generate_videos.py`
2. Download clips: `python download_videos.py`
3. Review in `output/` directory
