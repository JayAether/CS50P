def main():
    while True:
        try:
            fraction = input('Fraction: ')
            print(gauge(convert(fraction)))
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    fraction = fraction.split('/')
    fraction = [int(fraction[0]), int(fraction[1])]

    return round(fraction[0] / fraction[1] * 100)



def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif 100 >= percentage >= 99:
        return 'F'
    elif 99 > percentage > 1:
        return f"{percentage}%"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
