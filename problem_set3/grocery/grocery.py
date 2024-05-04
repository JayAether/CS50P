def main():
    groceries = get_list()
    for key, value in groceries.items():
        print(value, key)


# creat a list (dict actualy) of items inputed
# returns them sorted alphabeticly
def get_list():
    grocery_list = {}
    while True:
        try:
            item = input().upper().strip()
        except EOFError:
            return dict(sorted(grocery_list.items()))
        else:
            if not item in grocery_list:
                grocery_list[item] = 0
            grocery_list[item] += 1


main()
