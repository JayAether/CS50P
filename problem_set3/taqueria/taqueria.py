MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    get_order()


# infinitly take orders until ctr d
# after order is accepted print total
def get_order():
    total = 0.0
    while True:
        try:
            item = input('Item: ').title()
            if item in MENU:
                total += MENU[item]
                print(f'${total:.2f}')
        except EOFError:
            print()
            break


main()
