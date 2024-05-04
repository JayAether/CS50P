from pyfiglet import Figlet
import sys
from random import randint

figlet = Figlet()
font_list = figlet.getFonts()

def main():
    get_figlet()


def get_figlet():
    # if no args given. sets random font
    if len(sys.argv) == 1:
        chosen_font = font_list[randint(1, len(font_list))]
        figlet.setFont(font=chosen_font)

    # if args given.
    elif len(sys.argv) == 3:
        desired_font = sys.argv[2]
        flag = sys.argv[1]

        # error checker
        if not (flag in ('-f', '-font')):
            sys.exit('argument 1 must be either "-f" or "-font".')
        if not (desired_font in font_list):
            sys.exit('second argument must be a font.')

        # sets desired font
        chosen_font = font_list[font_list.index(desired_font)]
        figlet.setFont(font=chosen_font)

    else:
        sys.exit('argument parameter incomplete; please give either two arguments or none.')

    text = input('Input: ')
    print(figlet.renderText(text))


if __name__ == '__main__':
    main()
