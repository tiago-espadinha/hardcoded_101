import argparse
import os
import shutil
import json
import datetime
from pathlib import Path
from utils import logger, confirm

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".md", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".flac", ".aac"],
    "Code": [".py", ".js", ".ts", ".html", ".css", ".json", ".yaml"],
    "Archives": [".zip", ".tar", ".gz", ".7z", ".rar"],
    "Other": []
}

def get_category(ext):
    for category, extensions in FILE_TYPES.items():
        if ext.lower() in extensions:
            return category
    return "Other"

def organise(source, dest, dry_run=False):
    source_path = Path(source)
    dest_path = Path(dest)
    
    if not source_path.exists():
        logger.error(f"Source directory '{source}' does not exist.")
        return

    dest_path.mkdir(parents=True, exist_ok=True)
    moves = []

    for item in source_path.iterdir():
        if item.is_file() and not item.name.startswith(".organise_log_"):
            category = get_category(item.suffix)
            category_dir = dest_path / category
            
            target_path = category_dir / item.name
            
            if dry_run:
                logger.info(f"[DRY RUN] Would move: {item.name} -> {category}/{item.name}")
            else:
                category_dir.mkdir(exist_ok=True)
                # Handle filename collisions
                if target_path.exists():
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    target_path = category_dir / f"{item.stem}_{timestamp}{item.suffix}"
                
                shutil.move(str(item), str(target_path))
                moves.append({"from": str(item), "to": str(target_path)})
                logger.info(f"Moved: {item.name} -> {category}/")

    if moves:
        log_file = source_path / f".organise_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(log_file, "w") as f:
            json.dump(moves, f, indent=4)
        logger.info(f"Move log written to: {log_file}")

def undo(log_file, dry_run=False):
    log_path = Path(log_file)
    if not log_path.exists():
        logger.error(f"Log file '{log_file}' not found.")
        return

    with open(log_path, "r") as f:
        moves = json.load(f)

    for move in reversed(moves):
        src = Path(move["to"])
        dest = Path(move["from"])
        
        if dry_run:
            logger.info(f"[DRY RUN] Would undo: {src} -> {dest}")
        else:
            if src.exists():
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(src), str(dest))
                logger.info(f"Restored: {src} -> {dest}")
            else:
                logger.warn(f"File not found for undo: {src}")

def main():
    parser = argparse.ArgumentParser(description="Organise files in a directory by type.")
    parser.add_argument("--source", default=".", help="Directory to organise")
    parser.add_argument("--dest", help="Where to create folders (defaults to source)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen")
    parser.add_argument("--undo", help="Log file to reverse moves")

    args = parser.parse_args()
    dest = args.dest if args.dest else args.source

    if args.undo:
        if confirm.ask_yes_no(f"Reverse all moves from {args.undo}?"):
            undo(args.undo, args.dry_run)
    else:
        organise(args.source, dest, args.dry_run)

if __name__ == "__main__":
    main()
