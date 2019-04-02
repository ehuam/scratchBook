

from flask import Flask
from vsearch import search4letters

app = Flask(__name__)


@app.route('/hello')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4')
def do_search() -> str:
    phrase = 'life, the universe, and everything'
    letters = 'eiru,!'
    results = ''
    return results.join(search4letters(phrase=phrase, letters=letters))

@app.route('/search4_hf')
def do_search_hf() -> str:
    return str(search4letters('life, the universe, and everything', 'eiru,!'))


app.run()
