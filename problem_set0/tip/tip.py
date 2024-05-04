# main func
# take input as in pay and tip percent, then calculate tip based on desired tip percentage
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


# turn dollar string to float
# remove $
def dollars_to_float(dollars):
    dollars = dollars.replace('$', '')
    dollars = float(dollars)

    return dollars


# turn tip percent string to float
# remove % and make percentage 
def percent_to_float(percent):
    percent = percent.replace('%', '')
    percent = float(percent) / 100

    return percent


main()
