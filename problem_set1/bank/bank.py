# main func
# greets based on input
def main():
    greeting = input('Greeting: ').strip().split()

    greeting_price(greeting)



# check how much needs to be paid for the greeting
# 'Hello' == '$0' | any greeting beginning with 'H' == '$20' | anything else == '$0'
def greeting_price(greeting):
    if greeting[0] == 'Hello' or greeting[0] == 'Hello,':
        print('$0')
    elif greeting[0][0] == 'H':
        print('$20')
    else:
        print('$100')


main()

