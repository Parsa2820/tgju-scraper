'''
Retrieve price of currencies from tgju.org
'''

import sys
import requests
from bs4 import BeautifulSoup


USAGE = '''
Usage:
    python tgju.py --help # show this message
    python tgju.py --list # show list of currencies
    python tgju.py --all # show price of all currencies
    ptyhon tgju.py --ledger # show price of all currencies in ledger database format
    python tgju.py <currency> # show price of currency
    python tgju.py <currency1> <currency2> ... # show price of currencies
'''

CURRENCIES = {
    'USD': 'price_dollar_rl',
    'EUR': 'price_eur',
    'EMAMICOIN': 'sekee',
    'BAHARAZADICOIN': 'sekeb',
    'NIMCOIN': 'nim',
    'ROBICOIN': 'rob',
    'GERAMICOIN': 'gerami',
}


def get_price(target: str) -> float:
    '''
    Get price of target from tgju.org
    '''
    base_url = 'https://www.tgju.org/profile/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        'AppleWebKit/537.36 (KHTML, like Gecko)'
        'Chrome/70.0.3538.77 Safari/537.36'
    }

    url = f'{base_url}/{target}'
    response = requests.get(url=url, headers=headers, timeout=5)
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find_all('div', class_='header-items-p')
    for element in div:
        if len(element['class']) == 1:
            div = element
            break
    span = div.find('span', class_='value').contents[1]
    return float(span.text.replace(',', ''))


if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1] == '--help':
        print(USAGE)
    elif sys.argv[1] == '--list':
        for currency, _ in CURRENCIES.items():
            print(currency)
    elif sys.argv[1] == '--ledger':
        pass
    elif sys.argv[1] == '--all':
        for currency, key in CURRENCIES.items():
            price = get_price(key)
            print(f'{currency}: {price} IRR')
    else:
        for currency in sys.argv[1:]:
            if currency in CURRENCIES.keys():
                price = get_price(CURRENCIES[currency])
                print(f'{currency}: {price} IRR')
            else:
                print(f'Unknown currency: {currency}')
