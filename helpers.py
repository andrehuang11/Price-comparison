import requests
from bs4 import BeautifulSoup

def get_price_and_market(product_url):
    session = requests.Session()
    page = session.get(url=product_url)
    soup = BeautifulSoup(page.content,'lxml')
    if "sonda" in product_url:
        tag = soup.find('span', class_ = 'price')
        market = "Sonda"
        try:
            price = tag.text.strip()
        except:
            price = "Indisponível"
    else:
        tag = soup.find('div', class_ = 'current-pricesectionstyles__CurrentPrice-sc-17j9p6i-0 drikI')
        if "clubeextra" in product_url:
            market = "Extra"
            try:
                price = tag.text.strip()
            except AttributeError:
                price = "Indisponível"
        else:
            market = "Pão de açúcar"
            try:
                price = tag.text.strip()
            except AttributeError:
                price = "Indisponível"
    return price, market
