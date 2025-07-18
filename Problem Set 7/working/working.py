import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid format")

    h1, m1, p1, h2, m2, p2 = match.groups()
    m1 = m1 if m1 else "00"
    m2 = m2 if m2 else "00"

    if not (0 <= int(m1) < 60) or not (0 <= int(m2) < 60):
        raise ValueError("Invalid minutes")

    h1 = int(h1)
    h2 = int(h2)

    if not (1 <= h1 <= 12) or not (1 <= h2 <= 12):
        raise ValueError("Invalid hours")

    h1_24 = convert_hour(h1, p1)
    h2_24 = convert_hour(h2, p2)

    return f"{h1_24:02}:{m1} to {h2_24:02}:{m2}"

def convert_hour(hour, period):
    if period == "AM":
        return 0 if hour == 12 else hour
    else:  # PM
        return 12 if hour == 12 else hour + 12

if __name__ == "__main__":
    main()
