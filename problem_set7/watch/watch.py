import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    try:
        url = re.search(r'<iframe.*?youtube\.com(?:/embed)?(/\w+).*?></iframe>', s)
        if url:
            return f'https://youtu.be{url.group(1)}'
    except AttributeError:
        return None
    return None


if __name__ == "__main__":
    main()
