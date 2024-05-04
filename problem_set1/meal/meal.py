# main func
# tells you if it is meal time based on what time you put in
# can accept base 24 hour and 12 hour base, but needs you to put in am/pm after the time
# example, '14:43' for base 24. '2:43 pm' for base 12
def main():
    points = convert(input('What time is it? '))

    if 7 <= points <= 8:
        print('breakfast time')
    elif 12 <= points <= 13:
        print('lunch time')
    elif 18 <= points <= 19:
        print('dinner time')


# converts inputed time to comprehensible output 
def convert(time):
    hours, minutes = (time.split(':'))

    hours = float(hours)

    if 'am' in minutes or 'pm' in minutes:
        minutes, base = minutes.split(' ')
        if base == 'pm':
            hours += 12

    minutes = float(minutes)

    minutes = (minutes * (5 / 3)) / 100

    return hours + minutes


if __name__ == "__main__":
    main()
