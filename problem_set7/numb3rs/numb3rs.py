import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    try:
        numbs = re.search(r'^(\d+)\.(\d+)\.(\d+)\.(\d+)$', ip)
        for n in range(1, 5):
            if int(numbs.group(n)) > 255:
                return False
    except AttributeError:
        return False
    return True


if __name__ == "__main__":
    main()
