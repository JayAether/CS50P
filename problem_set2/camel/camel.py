# main func, :)
def main():
    camel_input = input('camelCase: ')

    print(camel_to_snake(camel_input))


# turns camel case to snake case
def camel_to_snake(camel_case):
    # base variable
    snake_sentance = ''

    # for loop going over every letter in camel_case,
    # if upper adds a '_' before adding the letters lower case, if lower adds letter
    for c in camel_case:
        if c.isupper():
            snake_sentance = snake_sentance + '_' + c.lower()
        else:
            snake_sentance = snake_sentance + c

    return 'snake_case: ' + snake_sentance


main()

