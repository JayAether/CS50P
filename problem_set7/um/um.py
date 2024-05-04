import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um_text = re.findall(r'\bum\b', s, flags=re.IGNORECASE)
    return len(um_text)


if __name__ == "__main__":
    main()
