# Module Name: automate-it

A collection of real-world Python automation tools designed to handle repetitive tasks like file organization, data cleaning, and web scraping.

## Features
- **File Organiser**: Sorts files into subdirectories by type with undo capability.
- **CSV Data Cleaner**: Configurable cleaning operations for CSV datasets.
- **Batch Image Resizer**: Parallelized image resizing and format conversion.
- **Web Scraper**: Configurable CSS selector-based scraper with robots.txt awareness.
- **Email Sender**: CLI-based email client supporting attachments and HTML templates.

## Learning Objectives
- Implement complex logic without relying on third-party magic.
- Understand the underlying mechanics of automation and I/O operations.
- Analyze performance characteristics using real-world benchmarks.

## Project Structure
- `organise.py`: File organization tool.
- `clean_csv.py`: CSV cleaning utility.
- `resize_images.py`: Image processing tool.
- `scrape.py`: Web scraping script.
- `send_email.py`: Email automation script.
- `utils/`: Shared utilities for logging, progress, and confirmation.

## Requirements
- Python 3.10+
- Pillow (for image resizing)
- BeautifulSoup4 and requests (for scraping)
- tqdm (optional, for progress bars)

## How to Run
Run the tools directly from the command line:
```bash
python organise.py --source ./downloads --dry-run
```

## Testing
Run all scripts with their respective help flags to see available options:
```bash
python clean_csv.py --help
```
