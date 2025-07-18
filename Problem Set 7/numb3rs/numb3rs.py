import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"
    matches = re.search(pattern, ip)
    if matches:
        for i in range(1,5):
            if int(matches.group(i)) <= 255:
                f= True
            else:
                return False
        return f
    else:
        return False



if __name__ == "__main__":
    main()