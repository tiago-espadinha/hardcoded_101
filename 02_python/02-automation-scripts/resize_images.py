import argparse
import os
import concurrent.futures
from pathlib import Path
from PIL import Image
from utils import logger, progress

try:
    from tqdm import tqdm
    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False

def resize_image(img_path, args):
    try:
        with Image.open(img_path) as img:
            original_width, original_height = img.size
            
            new_width = args.width
            new_height = args.height
            
            if args.max_size:
                max_w, max_h = map(int, args.max_size.split('x'))
                ratio = min(max_w / original_width, max_h / original_height)
                new_width = int(original_width * ratio)
                new_height = int(original_height * ratio)
            elif new_width and not new_height:
                new_height = int(original_height * (new_width / original_width))
            elif new_height and not new_width:
                new_width = int(original_width * (new_height / original_height))
            elif not new_width and not new_height:
                new_width, new_height = original_width, original_height

            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            output_dir = Path(args.output) if args.output else img_path.parent / "resized"
            output_dir.mkdir(parents=True, exist_ok=True)
            
            fmt = args.format if args.format else img.format
            ext = f".{fmt.lower()}" if args.format else img_path.suffix
            output_name = f"{img_path.stem}{args.suffix}{ext}"
            output_path = output_dir / output_name
            
            img.save(output_path, format=fmt, quality=args.quality)
            return True
    except Exception as e:
        logger.error(f"Error resizing {img_path.name}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Batch resize images.")
    parser.add_argument("directory", help="Directory containing images")
    parser.add_argument("--width", type=int, help="Target width")
    parser.add_argument("--height", type=int, help="Target height")
    parser.add_argument("--max-size", help="Bounding box (e.g. 1920x1080)")
    parser.add_argument("--quality", type=int, default=85, help="JPEG quality 1-95")
    parser.add_argument("--format", help="Convert to format (jpg, png, webp)")
    parser.add_argument("--suffix", default="_resized", help="Output filename suffix")
    parser.add_argument("--output", help="Output directory")

    args = parser.parse_args()
    dir_path = Path(args.directory)
    
    if not dir_path.exists():
        logger.error(f"Directory {args.directory} does not exist.")
        return

    img_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.gif'}
    img_files = [f for f in dir_path.iterdir() if f.suffix.lower() in img_extensions]
    
    if not img_files:
        logger.warn("No images found in the directory.")
        return

    logger.info(f"Processing {len(img_files)} images...")

    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(resize_image, img, args): img for img in img_files}
        
        if HAS_TQDM:
            for _ in tqdm(concurrent.futures.as_completed(futures), total=len(img_files), desc="Resizing"):
                pass
        else:
            completed = 0
            for _ in concurrent.futures.as_completed(futures):
                completed += 1
                progress.show_progress(completed, len(img_files), prefix="Progress:", suffix="Complete")

    logger.info("Batch resizing complete.")

if __name__ == "__main__":
    main()
