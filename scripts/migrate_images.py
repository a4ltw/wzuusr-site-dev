#!/usr/bin/env python3
"""
Image Migration Script for WZU USR Website
Downloads all images from Wix backup HTML files and organizes them locally.
"""

import os
import re
import json
import hashlib
import subprocess
import urllib.request
import urllib.error
from pathlib import Path
from html.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuration
WIX_BACKUP_DIR = Path(__file__).parent.parent / "wix_backup" / "usrdocument2018.wixsite.com" / "official"
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "assets" / "images"
MAPPING_FILE = Path(__file__).parent.parent / "scripts" / "image_mapping.json"

# Image URL patterns
WIX_IMAGE_PATTERN = re.compile(
    r'https://static\.wixstatic\.com/media/[a-zA-Z0-9_~]+\.(png|jpg|jpeg|gif|webp)(?:/[^"\s\)]+)?',
    re.IGNORECASE
)

# Category mapping based on file/URL patterns
CATEGORY_PATTERNS = {
    'team': ['team', '團隊', '計畫團隊', '教師', 'faculty'],
    'partners': ['合作夥伴', 'partner', 'logo'],
    'awards': ['award', '獎', 'trophy', 'expo'],
    'events/2020': ['2020'],
    'events/2021': ['2021'],
    'events/2022': ['2022'],
    'events/2023': ['2023'],
    'events/2025': ['2025'],
    'materials': ['教材', 'material', '繪本', 'animation'],
}


def extract_images_from_html(html_content: str) -> set:
    """Extract all Wix image URLs from HTML content."""
    images = set()

    # Pattern to capture complete image URLs including the final filename
    # Match: media/ID.ext/v1/fill/params/filename.ext or media/ID.ext/v1/crop/params/filename.ext
    full_pattern = re.compile(
        r'https://static\.wixstatic\.com/media/[a-zA-Z0-9_~]+(?:~mv2)?\.(png|jpg|jpeg|gif|webp)/v1/(?:fill|crop)/[^/]+/[^"\s\)\',]+\.(png|jpg|jpeg|gif|webp)',
        re.IGNORECASE
    )

    # Find full URLs with fill parameters (these work for downloading)
    for match in full_pattern.finditer(html_content):
        url = match.group(0)
        images.add(url)

    return images


def categorize_image(url: str, source_file: str) -> str:
    """Determine which category folder an image should go into."""
    url_lower = url.lower()
    source_lower = source_file.lower()
    combined = url_lower + source_lower

    for category, patterns in CATEGORY_PATTERNS.items():
        for pattern in patterns:
            if pattern.lower() in combined:
                return category

    # Default to events folder
    return 'events'


def get_image_filename(url: str) -> str:
    """Generate a clean filename from URL."""
    # Extract the media ID and extension from URL
    match = re.search(r'/media/([a-zA-Z0-9_~]+)\.(png|jpg|jpeg|gif|webp)', url, re.IGNORECASE)
    if match:
        media_id = match.group(1)
        ext = match.group(2).lower()

        # Shorten long IDs
        if len(media_id) > 30:
            # Use hash for uniqueness
            short_hash = hashlib.md5(media_id.encode()).hexdigest()[:8]
            media_id = media_id[:16] + '_' + short_hash
        return f"{media_id}.{ext}"

    # Fallback: use hash of URL
    url_hash = hashlib.md5(url.encode()).hexdigest()[:12]
    # Try to get extension from URL
    ext_match = re.search(r'\.(png|jpg|jpeg|gif|webp)', url, re.IGNORECASE)
    ext = ext_match.group(1).lower() if ext_match else 'jpg'
    return f"image_{url_hash}.{ext}"


def download_image(url: str, output_path: Path) -> tuple:
    """Download an image from URL to local path using curl."""
    if output_path.exists():
        return (url, str(output_path), 'skipped', 'File exists')

    try:
        # Create directory if needed
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Use curl with proper headers
        result = subprocess.run([
            'curl', '-s', '-L',
            '-H', 'Referer: https://usrdocument2018.wixsite.com/',
            '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            '-o', str(output_path),
            '-w', '%{http_code}',
            '--max-time', '30',
            url
        ], capture_output=True, text=True, timeout=60)

        http_code = result.stdout.strip()

        if http_code == '200':
            # Check file size
            if output_path.exists():
                size = output_path.stat().st_size
                if size > 100:
                    return (url, str(output_path), 'success', f'{size} bytes')
                else:
                    output_path.unlink()
                    return (url, str(output_path), 'error', 'Content too small')
            return (url, str(output_path), 'error', 'File not created')
        else:
            if output_path.exists():
                output_path.unlink()
            return (url, str(output_path), 'error', f'HTTP {http_code}')

    except subprocess.TimeoutExpired:
        return (url, str(output_path), 'error', 'Timeout')
    except Exception as e:
        return (url, str(output_path), 'error', str(e))


def main():
    """Main entry point."""
    print("=" * 60)
    print("WZU USR Image Migration Script")
    print("=" * 60)

    # Collect all HTML files
    html_files = list(WIX_BACKUP_DIR.rglob("*.html"))
    print(f"\nFound {len(html_files)} HTML files to process")

    # Extract all image URLs
    all_images = {}  # url -> source_file
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            images = extract_images_from_html(content)
            for img_url in images:
                if img_url not in all_images:
                    all_images[img_url] = str(html_file.relative_to(WIX_BACKUP_DIR))
        except Exception as e:
            print(f"Error reading {html_file}: {e}")

    # De-duplicate by base URL
    unique_images = {}
    for url, source in all_images.items():
        # Get base media ID
        match = re.search(r'/media/([a-zA-Z0-9_~]+)', url)
        if match:
            media_id = match.group(1)
            # Keep highest quality version (higher resolution)
            if media_id not in unique_images:
                unique_images[media_id] = (url, source)
            else:
                # Check if new URL has higher resolution
                old_url = unique_images[media_id][0]
                old_w = re.search(r'w_(\d+)', old_url)
                new_w = re.search(r'w_(\d+)', url)
                if old_w and new_w and int(new_w.group(1)) > int(old_w.group(1)):
                    unique_images[media_id] = (url, source)
        else:
            unique_images[url] = (url, source)

    print(f"Found {len(unique_images)} unique images")

    # Prepare download tasks
    download_tasks = []
    url_mapping = {}

    for media_id, (url, source) in unique_images.items():
        category = categorize_image(url, source)
        filename = get_image_filename(url)
        output_path = OUTPUT_DIR / category / filename

        download_tasks.append((url, output_path))
        url_mapping[url] = {
            'local_path': f"assets/images/{category}/{filename}",
            'source_file': source,
            'category': category
        }

    print(f"\nDownloading images to {OUTPUT_DIR}")
    print("-" * 60)

    # Download with progress
    success_count = 0
    skip_count = 0
    error_count = 0

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {
            executor.submit(download_image, url, path): url
            for url, path in download_tasks
        }

        for i, future in enumerate(as_completed(futures), 1):
            url, path, status, message = future.result()

            if status == 'success':
                success_count += 1
                print(f"[{i}/{len(futures)}] Downloaded: {Path(path).name}")
            elif status == 'skipped':
                skip_count += 1
                print(f"[{i}/{len(futures)}] Skipped: {Path(path).name}")
            else:
                error_count += 1
                print(f"[{i}/{len(futures)}] Error: {Path(path).name} - {message}")

    # Save mapping file
    with open(MAPPING_FILE, 'w', encoding='utf-8') as f:
        json.dump(url_mapping, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 60)
    print("Summary:")
    print(f"  Downloaded: {success_count}")
    print(f"  Skipped: {skip_count}")
    print(f"  Errors: {error_count}")
    print(f"  Mapping saved to: {MAPPING_FILE}")
    print("=" * 60)


if __name__ == '__main__':
    main()
