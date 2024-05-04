import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


# takes time in (5:00 AM to 9:00 PM) regexes turn to 24 hour base
def convert(s):
    try:
        clock = re.search(r'^(\d+)(?::)?(\d+)? (AM|PM) to (\d+)(?::)?(\d+)? (AM|PM)$', s)
        before = list(clock.group(1, 2, 3))
        after = list(clock.group(4, 5, 6))
    except AttributeError:
        raise ValueError

    before[0] = meridian_hour_manager(int(before[0]), before[2])
    after[0] = meridian_hour_manager(int(after[0]), after[2])
    before[1], after[1] = minute_manager(before[1]), minute_manager(after[1])

    return f'{before[0]:02}:{before[1]:02} to {after[0]:02}:{after[1]:02}'


# turns time from 12 base to 24 base
def meridian_hour_manager(hour, period):
    if period == 'PM' and hour != 12:
        return hour + 12
    if period == 'AM' and hour == 12:
        return hour - 12
    if hour > 12:
        raise ValueError
    return hour


# check if minute is between 0-60 and exists
def minute_manager(minute):
    if not minute:
        return 0
    if int(minute) >= 60:
        raise ValueError
    return int(minute)


if __name__ == "__main__":
    main()
