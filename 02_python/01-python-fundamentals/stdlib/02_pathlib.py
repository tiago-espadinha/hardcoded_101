"""
Demonstrates pathlib in Python.
Covers: Path operations, glob, recursive file walking
"""
from pathlib import Path

def main():
    # Current path
    cwd = Path.cwd()
    print(f"Current working directory: {cwd}")

    # Joining paths
    new_file = cwd / "test_pathlib.txt"
    print(f"Target file: {new_file}")

    # File operations
    new_file.write_text("Hello Pathlib!")
    print(f"Content: {new_file.read_text()}")
    
    # Check exists
    print(f"Exists: {new_file.exists()}")

    # Directory walking
    print("\nFiles in basics/ folder:")
    basics_dir = Path("basics")
    for f in basics_dir.glob("*.py"):
        print(f"- {f.name} (size: {f.stat().st_size} bytes)")

    # Cleanup
    new_file.unlink()

if __name__ == "__main__":
    main()
