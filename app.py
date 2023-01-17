from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    cat_api_url = "https://api.thecatapi.com/v1/images/search"
    cat_fact_url = "https://cat-fact.herokuapp.com/facts/random"

    cat_image_data = requests.get(cat_api_url).json()
    cat_fact_data = requests.get(cat_fact_url).json()

    cat_image = cat_image_data[0]["url"]
    cat_fact = cat_fact_data["text"]

    return render_template("index.html", cat_image=cat_image, cat_fact=cat_fact)

if __name__ == "__main__":
    app.run()
