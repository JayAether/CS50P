# list of the 20 most common fruits and their calories in accordance to the FDA
FDA_NUTRITION_SHEET = {'apple': '130', 'avocado': '50',
                       'banana': '110', 'cantaloupe': '50',
                       'grapefruit': '60', 'grapes': '90',
                       'honeydew melon': '50', 'kiwifruit': '90',
                       'lemon': '15', 'lime': '20',
                       'nectarine': '60', 'orange': '80',
                       'peach': '60', 'pear': '100',
                       'pineapple': '50', 'plums': '70',
                       'strawberries': '5   0', 'sweet cherries': '100',
                       'tangerine': '50', 'watermelon': '80'}

def main():
    get_fruit_nutrition()


# returns calories if input is in FDA_NUTRITION_SHEET, else return 0
def get_fruit_nutrition():
    x = input('Item: ').lower()

    if x in FDA_NUTRITION_SHEET:
        print(f'Calories: {FDA_NUTRITION_SHEET[x]}')
    else:
        return 0


main()
