def main():
    tweet = input("Input: ")
    print(shorten(tweet))


def shorten(word):
    tweet = ""
    vowels = ("i", "o", "a", "e", "u")
    for c in word:
        if not c.lower() in vowels:
            tweet += c
    return tweet


if __name__ == "__main__":
    main()
