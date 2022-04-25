# Price Checker for Non-perishables

<img src="Screenshots/main page.png" width="700">

> A price checker and comparison for top selling non-perishables in Brazil (rice, beans and coffee) on popular supermarkets (Sonda, Extra and Pão de açúcar), that gets data with a Web Scrapping script. Video Demo: https://youtu.be/_TFzf-PUmjU

##  Prerequisites
- Python
- Windows, Mac or Linux

##  Installing

Before running the application install the requirements of "requirements.txt":
```
pip install -r requirements.txt
```
If you get the error "bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?" you will need to install lxml with:
```
pip install lxml
```

##  Starting

To start the application run app.py

```
python app.py
```

## Usage
After starting the application go to http://127.0.0.1:8000. There you can check the prices of your products by selecting a product in "Escolha um produto" and clicking on "Pesquisar".
In the results page you can click on "Home" to get back to the main page.

## Files explanation
- Inside templates folder are the HTML files for each page of the website using Jinja as a template engine.
- app.py is the main file that runs the application using Flask.
- helpers.py is the file that contains the Web Scraper function.
- prices.py is the file that updates the database with sqlite3.
- database.db is the SQL database.

## Changing the code
Currently, to update prices you need to restart the entire application, but you can change the code on app.py to make prices update after each request. Warning: This change will make the website slower, because it will be scrapping data after each request.
- To make the changes just put the function "get_data()" inside the "home()" function. The code in app.py should look like this:
```
@app.route("/", methods=["GET", "POST"])
def home():
    get_data()

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
```
Now the app should update prices after each request.


## Tools
- Python
- Flask
- HTML
- Bootstrap
- BeautifulSoup4 for webscrapping
- SQL for database
