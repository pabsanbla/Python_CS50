import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    src = extract_src(s)
    if matches := re.search(r"^https?://(?:www\.)?youtube\.com/embed/(\w+)$", src):
        return "https://youtu.be/" + matches.group(1)
    else:
        return None

def extract_src(html):
    if match := re.search(r"<iframe[^>]+src=\"([^\"]+)\"", html):
        return match.group(1)
    else:
        return ""

if __name__ == "__main__":
    main()
