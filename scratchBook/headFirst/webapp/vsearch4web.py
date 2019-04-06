

from flask import Flask, render_template, request, redirect
from vsearch import search4letters

app = Flask(__name__)


@app.route('/')
def hello() -> 302:
    return redirect('/entry') 

@app.route('/search4_ed')
def do_search_ed() -> str:
    phrase = 'life, the universe, and everything'
    letters = 'eiru,!'
    results = ''
    return results.join(search4letters(phrase=phrase, letters=letters))


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Hare are your results'
    results = str(search4letters(phrase, letters))

    return render_template('results.html', 
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)


@app.route('/entry', methods=['GET'])
def entry_page() -> 'html':
    return render_template('entry.html',
                            the_title='Welcome to search4letters on the web!')


app.run(debug=True)
