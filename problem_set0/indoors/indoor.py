# main program
# lowers input
def main():
    x = input('what would you like to say? ')
    print(quiet(x))


# lowercase the paragraph
def quiet(yell):
    return yell.lower()


main()
