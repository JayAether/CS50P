import string


def main():
    greeting = input('greet: ')
    print(f'${value(greeting)}')


def value(greeting):
    punc = string.punctuation
    greeting = ''.join([c.lower() for c in greeting if c not in punc]).split()

    if len(greeting) < 1:
        return 100
    if greeting[0] == 'hello':
        return 0
    elif greeting[0][0] == 'h':
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
