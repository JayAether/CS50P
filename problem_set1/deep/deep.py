# main func
#
def main():
    answer = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')
    answer = answer.strip().lower()

    life_answer(answer)


# check if answer is 42 (or it's subsequent)
def life_answer(answer):

    match answer:
        case '42' | 'forty-two' | 'forty two':
            print('yes')
        case _:
            print('no')


main()
