# main func
# asks input then slows it down
def main():
    x = input('speak, child!! ')
    print(slowdown(x))


# turns 'this is a sentence' to 'this...is...a...sentence'
def slowdown(speed_talk):
    return speed_talk.replace(' ', '...')


main()
