from flask import Flask, render_template, request
from scraper import scrape_category

app = Flask(__name__)

categories = {
    "Electronique": "https://www.aliexpress.com/category/44/consumer-electronics.html?sortType=total_tranpro_desc",
    "Mode Femme": "https://www.aliexpress.com/category/100003109/women-clothing.html?sortType=total_tranpro_desc",
    "Maison & Jardin": "https://www.aliexpress.com/category/15/home-garden.html?sortType=total_tranpro_desc",
    "Beauté": "https://www.aliexpress.com/category/66/beauty-health.html?sortType=total_tranpro_desc"
}

@app.route("/", methods=["GET", "POST"])
def index():
    results = []

    if request.method == "POST":
        selected = request.form.get("category")
        url = categories.get(selected)
        if url:
            results = scrape_category(url)

    return render_template("index.html", categories=categories.keys(), results=results)

if __name__ == "__main__":
    app.run(debug=True)
