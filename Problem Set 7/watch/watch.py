import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"^<iframe src=\"https?://(?:www\.)?youtube\.com/embed/(\w+)\""
    if matches := re.search(pattern, s):
        ans = f"https://youtu.be/{matches.group(1)}"
        return ans





if __name__ == "__main__":
    main()