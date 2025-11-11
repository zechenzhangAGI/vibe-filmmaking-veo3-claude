#!/usr/bin/env python3
"""
Download generated video clips from URLs stored in metadata.
"""

import json
import requests
from pathlib import Path
from typing import Dict, Any

OUTPUT_DIR = Path(__file__).parent.parent / "output"
METADATA_FILE = OUTPUT_DIR / "generation_metadata.json"


def load_metadata() -> Dict[str, Any]:
    """Load generation metadata"""
    if not METADATA_FILE.exists():
        raise FileNotFoundError(f"Metadata file not found: {METADATA_FILE}")

    with open(METADATA_FILE, 'r') as f:
        return json.load(f)


def download_clip(clip_id: str, video_url: str, output_path: Path) -> bool:
    """
    Download a single video clip

    Args:
        clip_id: Clip identifier
        video_url: URL to download from
        output_path: Local path to save video

    Returns:
        True if successful, False otherwise
    """
    if output_path.exists():
        print(f"⏭️  {clip_id}: Already downloaded, skipping")
        return True

    try:
        print(f"⬇️  Downloading {clip_id}...")

        response = requests.get(video_url, stream=True, timeout=300)
        response.raise_for_status()

        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0

        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Progress indicator
                    if total_size > 0:
                        progress = (downloaded / total_size) * 100
                        print(f"   Progress: {progress:.1f}%", end='\r')

        print(f"\n✅ {clip_id}: Downloaded successfully")
        return True

    except Exception as e:
        print(f"\n❌ {clip_id}: Download failed - {str(e)}")
        if output_path.exists():
            output_path.unlink()  # Remove partial download
        return False


def main():
    """Main download function"""

    print("📥 Orchestra Video Clip Downloader")
    print("="*60)

    # Load metadata
    try:
        metadata = load_metadata()
    except FileNotFoundError as e:
        print(f"❌ {str(e)}")
        print("\nRun generate_videos.py first to generate clips.")
        return

    clips = metadata.get("clips", {})
    if not clips:
        print("❌ No clips found in metadata")
        return

    print(f"\nFound {len(clips)} clips to download\n")

    # Download each clip
    success_count = 0
    failed_clips = []

    for clip_id, clip_data in clips.items():
        video_url = clip_data.get("video_url")

        if not video_url:
            print(f"⚠️  {clip_id}: No video URL in metadata, skipping")
            failed_clips.append(clip_id)
            continue

        # Determine file extension from URL or default to mp4
        ext = ".mp4"
        if "." in video_url.split("/")[-1]:
            ext = "." + video_url.split(".")[-1].split("?")[0]

        output_path = OUTPUT_DIR / f"{clip_id}{ext}"

        if download_clip(clip_id, video_url, output_path):
            success_count += 1
        else:
            failed_clips.append(clip_id)

        print()  # Blank line between downloads

    # Summary
    print("="*60)
    print(f"\n📊 Download Summary:")
    print(f"   ✅ Successful: {success_count}/{len(clips)}")

    if failed_clips:
        print(f"   ❌ Failed: {len(failed_clips)}")
        print(f"\nFailed clips:")
        for clip_id in failed_clips:
            print(f"   - {clip_id}")
    else:
        print(f"\n🎉 All clips downloaded successfully!")

    print(f"\n📁 Output directory: {OUTPUT_DIR}")
    print("="*60)


if __name__ == "__main__":
    main()
