# convert mass given to energy (in accordance to einsteins thingy)
# E = mc^2
def convert(mass):
    SPEED_OF_LIGHT = 300000000
    e = mass * SPEED_OF_LIGHT ** 2
    return e


# main func
# calls convert to take mass, then return energy
def main():
    x = convert(int(input('m: ')))
    print('e:', x)


main()
