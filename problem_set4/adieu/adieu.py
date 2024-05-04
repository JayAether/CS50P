def main():
    name_list = get_names()
    create_goodbye(name_list)


# get the names
def get_names():
    name_list = []

    while True:
        try:
            name = input("Name: ").strip()
            name_list.append(name)
        except EOFError:
            print()
            return name_list


# prints out the 'adieu' to the names given
def create_goodbye(name_list):
    goodbye_sentance = "Adieu, adieu, "

    goodbye_sentance += f"to {name_list[0]}"
    if len(name_list) > 2:
        goodbye_sentance += ","
        for name in name_list[1:-1]:
            print(name)
            goodbye_sentance += f" {name},"
    if len(name_list) > 1:
        goodbye_sentance += f" and {name_list[-1]}"

    print(goodbye_sentance)


if __name__ == "__main__":
    main()
