from requests import get, RequestException
from sys import exit, argv


def main():
    amount = get_bitcoin_rate() * get_coin_count()
    print(f'${amount:,.4f}')


# get the coin count as an argv[1]
def get_coin_count():
    try:
        coins = argv[1]
        if is_number(coins):
            return float(coins)
        exit('Command-line argument is not a number')
    except IndexError:
        exit('Missing command-line argument')


# get the bitcoin price
def get_bitcoin_rate():
    try:
        data = get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
        price = data['bpi']['USD']['rate']
    except RequestException as request_error:
        print(request_error)
    return float(price.replace(",", ""))


# check if it is a number
def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    main()
