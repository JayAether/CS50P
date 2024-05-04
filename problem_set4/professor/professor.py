import random


def main():
    equations = generate_integer(get_level())
    score = 0

    # runs 10 times. each time you have to answer an equation
    for i in range(10):
        current_equation = f'{equations[i][0]} + {equations[i][1]} = '
        z = str(equations[i][0] + equations[i][1])

        # runs thrice per equation and gives answer if three strikes are gained
        for strike in range(3):
            if input(current_equation) != z:
                print('EEE')
                if strike == 2:
                    print(current_equation + z)
                continue
            else:
                score += 1
                break

    print(f'Score: {score}')


# get level of difficulty from user
def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if not (level in (1, 2, 3)):
                raise ValueError
            return level
        except ValueError:
            pass


# generate ten lists in a list, with each list having two numbers
def generate_integer(level):
    equation_list = []

    # runs 10 times.
    # gives x y in singles, dozens, then hundreds based on level (1, 2, 3 acordingly)
    for _ in range(10):
        equation = []

        if level == 1:
            equation.append(random.randint(0, 9))
            equation.append(random.randint(0, 9))
        elif level == 2:
            equation.append(random.randint(10, 99))
            equation.append(random.randint(10, 99))
        else:
            equation.append(random.randint(100, 999))
            equation.append(random.randint(100, 999))

        equation_list.append(equation)
    return equation_list


if __name__ == "__main__":
    main()
