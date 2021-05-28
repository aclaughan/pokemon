import requests
import lxml.html as lh
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, filename="app.log")


def main():
    url = 'http://pokemondb.net/pokedex/all'

    header = {}

    r = requests.get(url, headers=header)
    df = pd.read_html(r.text)[0]

    print(df.head())


if __name__ == '__main__':
    main()

# logging.debug(stuff)
