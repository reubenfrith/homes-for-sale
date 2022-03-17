from cgitb import html
from crypt import methods
from operator import methodcaller
from flask import Flask, render_template, url_for, redirect, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    postcode = request.form.get("query")


    if len(str(postcode))>4 or len(str(postcode))<4 or str(postcode).isnumeric()==False:

      return render_template('index.html')

    url = f"https://www.allhomes.com.au/sale/search?page=1&postcode={postcode}"
    response = requests.get(url)
    html = response.content
    scraped = BeautifulSoup(html, 'html.parser')

    pages_num = scraped.find_all(class_ = 'css-3ebg57')
    pages=[1]
    for x in pages_num:
      pages.append(int(x.get_text()))
    last_page = max(pages)

    for x in range(0,last_page):
      url = f"https://www.allhomes.com.au/sale/search?page={x}&postcode={postcode}"
      response = requests.get(url)
      html = response.content
      scraped = BeautifulSoup(html, 'html.parser')

      houses = scraped.find_all(class_ = 'css-1l8qi96')

      list_of_houses = []

      for y in houses:
        house = y.get_text()
        list_of_houses.append(house)
    return render_template('results.html', list_of_houses = list_of_houses)


  return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
