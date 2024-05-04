def main():
    coke_price = 50

    calculate_remainder(coke_price)


# infinitly request coin until coin is valid
def get_coin(remainder):
    while True:
        # remind how much is left
        print(f'Amount Due: {remainder}')

        # get input then check if coin is valid
        coin = input('Insert Coin: ')
        if coin in ('5', '10', '25'):
            return int(coin)


# infinitely calculate remainder based on coin gotten from get_coin()
def calculate_remainder(remainder):
    # keep getting coins unil remainder <= 0
    while remainder > 0:
        coin = get_coin(remainder)

        remainder = remainder - coin

    # returns how much you are owed after you fully pay
    print(f'Change Owed: {abs(remainder)}')


main()


