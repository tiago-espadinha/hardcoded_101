import argparse
import csv
import re
import os
from pathlib import Path
from utils import logger

def snake_case(s):
    s = s.strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[-\s]+', '_', s).lower()
    return s

def clean_csv(input_file, args):
    input_path = Path(input_file)
    output_file = args.output if args.output else f"{input_path.stem}_cleaned.csv"
    
    rows_before = 0
    rows_after = 0
    columns_renamed = 0
    cells_changed = 0

    try:
        with open(input_path, mode='r', encoding=args.encoding, newline='') as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames
            original_headers = list(headers)
            
            if args.normalise_headers:
                headers = [snake_case(h) for h in headers]
                columns_renamed = sum(1 for o, n in zip(original_headers, headers) if o != n)
            
            cleaned_rows = []
            for row in reader:
                rows_before += 1
                new_row = {}
                
                is_empty_row = True
                for i, (key, value) in enumerate(row.items()):
                    new_key = headers[i]
                    cleaned_val = value
                    
                    if args.strip_whitespace:
                        cleaned_val = cleaned_val.strip()
                    
                    if not cleaned_val and args.fill_empty:
                        cleaned_val = args.fill_empty
                    
                    if cleaned_val != value:
                        cells_changed += 1
                        
                    if cleaned_val:
                        is_empty_row = False
                    
                    new_row[new_key] = cleaned_val
                
                if args.drop_empty_rows and is_empty_row:
                    continue
                
                cleaned_rows.append(new_row)

            if args.drop_duplicates:
                unique_rows = []
                seen = set()
                for row in cleaned_rows:
                    row_tuple = tuple(row.items())
                    if row_tuple not in seen:
                        seen.add(row_tuple)
                        unique_rows.append(row)
                cleaned_rows = unique_rows

            rows_after = len(cleaned_rows)

            with open(output_file, mode='w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader()
                writer.writerows(cleaned_rows)

            logger.info(f"Cleaned CSV saved to: {output_file}")
            print("\nSummary:")
            print(f"- Rows before:      {rows_before}")
            print(f"- Rows after:       {rows_after}")
            print(f"- Columns renamed:  {columns_renamed}")
            print(f"- Cells changed:    {cells_changed}")

    except Exception as e:
        logger.error(f"Error cleaning CSV: {e}")

def main():
    parser = argparse.ArgumentParser(description="Clean and normalise CSV files.")
    parser.add_argument("input", help="CSV file to clean")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--strip-whitespace", action="store_true", help="Strip whitespace from cells")
    parser.add_argument("--normalise-headers", action="store_true", help="Snake_case header names")
    parser.add_argument("--drop-empty-rows", action="store_true", help="Remove empty rows")
    parser.add_argument("--drop-duplicates", action="store_true", help="Remove duplicate rows")
    parser.add_argument("--fill-empty", help="Fill empty cells with this string")
    parser.add_argument("--encoding", default="utf-8-sig", help="Input encoding (default: utf-8-sig)")

    args = parser.parse_args()
    clean_csv(args.input, args)

if __name__ == "__main__":
    main()
