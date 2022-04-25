from flask import Flask, render_template, request
import sqlite3
from prices import get_data

conn = sqlite3.connect('database.db', check_same_thread=False)
c = conn.cursor()

app = Flask(__name__)

get_data()

@app.route("/", methods=["GET", "POST"])
def home():

    c.execute('''SELECT produto FROM database GROUP BY produto''')
    products = c.fetchall()
    
    if request.method == "POST":
        
        product = request.form.get("product")
        
        if not product:
            return render_template("home.html", products=products)
        
        c.execute('''SELECT preço, mercado FROM database WHERE produto = ?''', (product,))
        results = c.fetchall()
        
        return render_template("results.html", results=results, product=product)

    else:
        return render_template("home.html", products=products)

if __name__ == "__main__":
  app.run(port = 8000, debug = False)
