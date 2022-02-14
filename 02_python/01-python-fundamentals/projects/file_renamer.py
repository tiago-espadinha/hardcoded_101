"""
CLI Tool: File Renamer.
Features: Given a directory and a pattern, preview changes, ask for confirmation, rename.
Patterns: add prefix, change extension, sequential numbering.
"""
import os
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Bulk file renamer")
    parser.add_argument("dir", help="Directory to process")
    parser.add_argument("--prefix", help="Add prefix to files")
    parser.add_argument("--ext", help="Change file extension")
    parser.add_argument("--seq", action="store_true", help="Sequential numbering")
    
    args = parser.parse_args()
    path = Path(args.dir)
    
    if not path.is_dir():
        print(f"Error: {args.dir} is not a directory")
        return

    files = [f for f in path.iterdir() if f.is_file()]
    renames = []

    for i, f in enumerate(files):
        new_stem = f.stem
        new_suffix = f.suffix
        
        if args.prefix:
            new_stem = f"{args.prefix}{new_stem}"
        if args.seq:
            new_stem = f"{new_stem}_{i+1:03d}"
        if args.ext:
            new_suffix = f".{args.ext.lstrip('.')}"
        
        new_name = f"{new_stem}{new_suffix}"
        if new_name != f.name:
            renames.append((f, path / new_name))

    if not renames:
        print("No changes needed.")
        return

    print("Preview of changes:")
    for old, new in renames:
        print(f"  {old.name} -> {new.name}")

    confirm = input("Proceed with rename? (y/n): ").strip().lower()
    if confirm == 'y':
        for old, new in renames:
            old.rename(new)
        print(f"Successfully renamed {len(renames)} files.")
    else:
        print("Aborted.")

if __name__ == "__main__":
    main()
