def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # check if length inbetween 2 and 6
    if not (2 <= len(s) <= 6):
        return False

    # check if first two characters are alpha
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    first_digit_checked = False
    for c in s:
        # check if c is a valid character
        if c in (' ', ',', '.'):
            return False

        # return False if an alpha is infront of digit
        if c.isalpha() and first_digit_checked:
            return False

        # only trigers on finding a digit for the first time
        # return False if first digit in plate is zero
        if c.isdigit() and not first_digit_checked:
            if c == '0':
                return False
            first_digit_checked = True

    return True


main()
