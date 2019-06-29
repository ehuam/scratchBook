

from flask import Flask, render_template, request, escape 
from vsearch import search4letters
from DBcm import UseDatabase

app = Flask(__name__)
# app.config is a dictionary of variables
app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB',}


def log_request(req: 'flask_request', res: str) -> None:
    with UseDatabase(app.config['dbconfig']) as cursor:
        # create a string containg the query you want to use
        _SQL = """insert into log
               (phrase, letters, ip, browser_string, results)
               values
               (%s, %s, %s, %s, %s)"""
        # execute the query
        # rather than store the entire browser string (stored in req.user_agent)
        # we only extract the name of the brower with req.user_agent.attribute
        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,  # extract name of browser
                              res, ))

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Hare are your results'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)


@app.route('/')
@app.route('/entry', methods=['GET'])
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')



@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with UseDatabase(app.config['dbconfig']) as cursor:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':
    app.run(debug=True)
