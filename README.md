# tgju-scraper

A simple scraper for [tgju.org](https://www.tgju.org/) with command line interface.

## Requirements
- Python 3.6+
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

## Usage
There is no installation option yet, so you have to clone the repository and run the script manually.
I may package it in the future.

```bash
git clone https://github.com/Parsa2820/tgju-scraper.git
cd tgju-scraper
python3 tgju.py --help
```
```bash
Usage:
    python tgju.py --help # show this message
    python tgju.py --list # show list of currencies
    python tgju.py --all # show price of all currencies
    ptyhon tgju.py --ledger # show price of all currencies in ledger database format
    python tgju.py <currency> # show price of currency
    python tgju.py <currency1> <currency2> ... # show price of currencies
```

> What is ledger database format?
> Ledger is a double-entry accounting system. It is kinda cool. Check it out [here](https://www.ledger-cli.org/).
> This option is useful if you want to convert the prices in your ledger file to IRR.
