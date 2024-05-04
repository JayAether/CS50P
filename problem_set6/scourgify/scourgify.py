import csv, sys


def main():
    invalidity()
    file = get_old_file()
    write_new_file(file)


def invalidity():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    try:
        with open(sys.argv[1]):
            pass
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')


def get_old_file():
    information = []
    with open(sys.argv[1]) as file:
        file = csv.DictReader(file)
        for row in file:
            last, first = row['name'].split(',')
            information.append({'first': first, 'last': last.strip(), 'house': row['house']})

    return information


def write_new_file(file):
    with open(sys.argv[2], 'w', newline='') as csvfile:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in file:
            writer.writerow({fieldnames[0]: row['first'].strip(), fieldnames[1]: row['last'].strip(), fieldnames[2]: row['house'].strip()})


if __name__ == '__main__':
    main()
