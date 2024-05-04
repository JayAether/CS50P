import csv
from sys import exit, argv
from tabulate import tabulate


def main():
    validity()
    menu = get_menu()
    print(tabulate(menu[1:], headers=menu[0], tablefmt="grid"))


def validity():
    if len(argv) < 2:
        exit('Too few command-line arguments')
    if len(argv) > 2:
        exit('Too many command-line arguments')

    if not argv[1].endswith('.csv'):
        exit('Not a CSV file')

    try:
        with open(argv[1]):
            pass
    except FileNotFoundError:
        exit('File does not exist')


def get_menu():
    menu = []
    with open(argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            menu.append([row[0], row[1], row[2]])

    return menu


if __name__ == '__main__':
    main()
