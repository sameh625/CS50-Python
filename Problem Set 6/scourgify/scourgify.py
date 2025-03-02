import sys
import csv

def main():
    validate()
    f1, f2 = sys.argv[1], sys.argv[2]
    try:
        with open(f1, "r") as file1, open(f2, "w") as file2:
            reader = csv.DictReader(file1)
            writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({"first": first, "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

def validate():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
            sys.exit("Not a CSV file")

main()
