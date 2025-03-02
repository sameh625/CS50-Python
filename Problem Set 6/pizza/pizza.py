import csv
import sys
from tabulate import tabulate


def main():
    validate()
    f = sys.argv[1]
    menu = []
    try:
        with open(f, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu.append(row)
            print(tabulate(menu, headers="keys" ,tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")



def validate():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if "csv" not in sys.argv[1].split("."):
            sys.exit("Not a CSV file ")
if __name__ == "__main__":
    main()
