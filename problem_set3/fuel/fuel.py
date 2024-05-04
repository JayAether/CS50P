def main():
    gauge = get_fuel()
    print(gauge)


# infinitly prompt user for fuel gaugereturn
# return 'f' (full), 'e' (empty), or the percentage
def get_fuel():
    while True:
        try:
            fraction = input('Fraction: ').split('/')
            fraction = [int(f) for f in fraction]
            fraction = fraction[0] / fraction[1]
            if fraction > 1:
                continue
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if fraction <= 0.01:
                return 'E'
            if fraction >= 0.99:
                return 'F'
            return str(round(fraction * 100)) + '%'


main()
