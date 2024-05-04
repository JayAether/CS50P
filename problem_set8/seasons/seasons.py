from datetime import date, timedelta
import inflect
import re
import sys

p = inflect.engine()


def main():
    user_date = input('Date of Birth: ')
    dat = get_date(user_date)
    print(become_minute_words(get_diff(dat)))


def get_date(user_date):
    if search := re.search(r'^(\d{1,4})-(\d{1,2})-(\d{1,2})$', user_date):
        user_date = list(map(int, search.groups()))
    else:
        sys.exit('Invalid date')

    date_validity(user_date)
    return user_date



def date_validity(dat):
    if 0 > dat[0] > 9999:
        sys.exit('Invalid date')
    if 1 > dat[1] < 12:
        sys.exit('Invalid date')
    if 1 > dat[2] > 31:
        sys.exit('Invalid date')


def get_diff(dat):
    today = date.today()
    birth_day = date(dat[0], dat[1], dat[2])
    return (today - birth_day).days



def become_minute_words(day):
    minutes = p.number_to_words(day * 24 * 60).replace(' and', '')
    return f'{minutes} minutes'.capitalize()


if __name__ == "__main__":
    main()

