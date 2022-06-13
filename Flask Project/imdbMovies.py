from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('imdbsearch.html')


@app.route("/succes", methods=['POST'])
def movies():
    movieNo = request.form.get('movieNumber')
    Req = requests.get(
        "https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&count="+movieNo)
    source = BeautifulSoup(Req.content, "html.parser")
    return render_template("movies.html", source=source, movieNo=movieNo)


if __name__ == '__main__':
    app.run()
