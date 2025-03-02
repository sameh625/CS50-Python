import sys

size = 0

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if "py" not in sys.argv[1].split("."):
        sys.exit("Not a Python file ")
    else:
        f = sys.argv[1]
        try:
            with open(f, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.strip().startswith("#") or line.isspace():
                        continue
                    else:
                        size += 1
        except FileNotFoundError:
            sys.exit("File does not exist")

        print(size)
