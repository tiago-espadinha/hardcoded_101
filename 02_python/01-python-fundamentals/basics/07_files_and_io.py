"""
Demonstrates Files and IO in Python.
Covers: open/read/write/append, with statement, csv module, json module
"""
import csv
import json

def main():
    # Simple file writing
    with open("test.txt", "w") as f:
        f.write("Line 1\n")
        f.write("Line 2\n")

    # Appending
    with open("test.txt", "a") as f:
        f.write("Line 3 appended\n")

    # Reading
    with open("test.txt", "r") as f:
        print(f"File content:\n{f.read()}")

    # Exercise: Student grades (CSV to JSON)
    students = [
        {"name": "Alice", "math": 85, "science": 92},
        {"name": "Bob", "math": 78, "science": 75},
        {"name": "Charlie", "math": 90, "science": 88},
    ]

    csv_file = "grades.csv"
    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "math", "science"])
        writer.writeheader()
        writer.writerows(students)

    # Process CSV and compute averages
    summary = []
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            avg = (int(row["math"]) + int(row["science"])) / 2
            summary.append({
                "name": row["name"],
                "average": avg
            })

    # Write summary to JSON
    json_file = "summary.json"
    with open(json_file, "w") as f:
        json.dump(summary, f, indent=4)

    print(f"Summary JSON:\n{open(json_file).read()}")

if __name__ == "__main__":
    main()
