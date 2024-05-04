from sys import argv, exit


def main():
    validity()
    print(count_lines())


# check if- only one arg given | arg is py | arg exists as a file
def validity():
    if len(argv) < 2:
        exit('Too few command-line arguments')
    elif len(argv) > 2:
        exit('Too many command-line arguments')
    if not argv[1].endswith('.py'):
        exit('Not a Python file')
    try:
        with open(argv[1]):
            pass
    except FileNotFoundError:
        exit('File does not exist')


# count the total lines of code in the file. skips '#' and empty spaces
def count_lines():
    total_lines = 0
    with open(argv[1]) as file:
        for line in file:
            if line.strip():
                if line.strip()[0] != '#':
                    total_lines += 1

    return total_lines


if __name__ == '__main__':
    main()
