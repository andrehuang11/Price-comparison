import sqlite3
from helpers import get_price_and_market

def get_data():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''SELECT url FROM database''')
    urls = c.fetchall()

    for url in urls:
        if "arroz" in url[0].lower():
            price, market = get_price_and_market(url[0])
            product = "Arroz Camil 5kg"
        elif "feij" in url[0].lower():
            price, market = get_price_and_market(url[0])
            product = "Feijão carioca Camil 1kg"
        else:
            price, market = get_price_and_market(url[0])
            product = "Café Melitta 500g"

        c.execute('''UPDATE database SET produto = ?, preço = ?, mercado = ?  WHERE url = ?''', (product, price, market, url[0]))
        conn.commit()
        
    conn.close()
