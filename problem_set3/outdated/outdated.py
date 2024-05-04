def main():
    get_date()


# infinitly asks for date,
# only accepts input in mm/dd/yyyy format and returns yyyy/mm/dd
def get_date():
    month_list = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]

    # gets input
    while True:
        try:
            user_date = input('Date: ').strip()
        except EOFError:
            break

        # after getting input, checks if checks multiple conditions before printing yyyy-mm-dd
        try:
            date_held = user_date.replace('/', ' ').replace(',', '')
            month, day, year = date_held.split(' ')

            if month.isalpha():
                if not (',' in user_date):
                    continue
                if month.lower() in month_list:
                    month = month_list.index(month.lower()) + 1
            else:
                month = int(month)
                if month > 12:
                    continue

            if int(day) > 31:
                continue

            print(f'{year}-{month:02}-{int(day):02}')
            break
        except (ValueError, IndexError):
            pass


main()
