def main():
    plate = input('your plate: ')
    if is_valid(plate):
        print('VALID')
    else:
        print('INVALID')


def is_valid(s):
    invalid_characters = (' ', ',', '.')
    has_num = False

    # error checker
    if not (2 <= len(s) <= 6):
        return False
    if s[0].isdigit() or s[1].isdigit():
        return False
    
    for c in s:
        if c in invalid_characters:
            return False
        if c.isdigit():
            if not has_num and c == '0':
                return False
            has_num = True
        elif has_num:
            return False

    return True


if __name__ == "__main__":
    main()
