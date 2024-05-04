# main func
def main():
    math_interpreter(input('expresion: '))


# completes math equation
def math_interpreter(equation):
    equation = equation.split()

    # seperate equation to x y z
    x = float(equation[0])
    y = equation[1]
    z = float(equation[2])

    if y == '+':
        print(x + z)
    elif y == '-':
        print(x - z)
    elif y == '*':
        print(x * z)
    elif y == '/':
        print(x / z)


main()
