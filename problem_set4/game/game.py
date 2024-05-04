from random import randint

def main():
    guess_game()


# returns randint between 1 and input
def get_level():
    while True:
        try:
            n = int(input('Level: '))
            if n > 0:
                return randint(1, n)
        except ValueError:
            pass


# makes you guess the num while giving hints
def guess_game():
    n = get_level()

    while True:
        try:
            guess = int(input('guess: '))
        except ValueError:
            pass
        else:
            if guess > n:
                print('too large!')
            elif guess < n:
                print('too small!')
            else:
                print('just right!')
                break


if __name__ == '__main__':
    main()
