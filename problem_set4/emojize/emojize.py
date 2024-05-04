import emoji

def main():
    emoji_index()


def emoji_index():
    emo = input('input: ')

    emo = emoji.emojize(emo)
    emo = emoji.emojize(emo, language='alias')

    print(emo)


if __name__ == '__main__':
    main()

