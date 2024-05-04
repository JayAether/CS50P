# vowel list
VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

def main():
    twitter = input('Input: ')

    remove_vowels(twitter)


def remove_vowels(twitter):
    # final sentance
    twttr = ''

    # cicle every character in twitter var
    for c in twitter:

        # continue if c is a vowel, if not add to twttr
        if c in VOWELS:
            continue
        else:
            twttr = twttr + c

    print(f'Output: {twttr}')


main()
