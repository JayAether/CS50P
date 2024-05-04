# turn emoticons to emojis
def convert(sentance):
    sentance = sentance.replace(':(', '🙁')
    sentance = sentance.replace(':)', '🙂')
    return sentance


# main func
# take input, use emoticons to emojis
def main():
    x = input()
    print(convert(x))


main()
