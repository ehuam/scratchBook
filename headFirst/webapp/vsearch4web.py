from flask import Flask, render_template, request, escape, session
from flask import copy_current_request_context
from vsearch import search4letters

from DBcm import UseDatabase, ConnectionError, CredentialsError
from checker import check_logged_in

from threading import Thread
from time import sleep


app = Flask(__name__)
# app.config is a dictionary of variables
app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB', }
# Debug Questions: what if the database connection fails?
# Database Interface error is raised. 

app.secret_key = 'YouWillNeverGuessMySecretKey'

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out.'

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':

    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        sleep(15) # This makes log_request really slow
        with UseDatabase(app.config['dbconfig']) as cursor:
        # create a string containg the query you want to use
            _SQL = """insert into log
                    (phrase, letters, ip, browser_string, results)
                    values
                    (%s, %s, %s, %s, %s)"""
        # execute the query
        # Rather than store the entire browser string
        # (stored in req.user_agent)
        # We only extract the name of the brower
        # with req.user_agent.attribute
            cursor.execute(_SQL, (req.form['phrase'],
                        req.form['letters'],
                        req.remote_addr,
                        req.user_agent.browser,
                        res,))

    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Hare are your results'
    results = str(search4letters(phrase, letters))

    try:
        t=Thread(target=log_request, args=(request, results)) 
        t.start()
    except Exception as err:
        print('***** logging failed with {}:.'.format(err))

    return render_template('results.html',
                          the_phrase=phrase,
                          the_title=title,
                          the_letters=letters,
                          the_results=results,)

    #Debug question: What happens if log_request call fails?

@app.route('/')
@app.route('/entry', methods=['GET'])
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')

    # Debug question: SQL protected from web-based attacks? 
    # Such as sql injection or Cross site scripting?

@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """Select phrase, letters, ip, browser_string, results FROM
                      log"""

            cursor.execute(_SQL)
            contents = cursor.fetchall()

        titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
        return render_template('viewlog.html',
                               the_title='View Log',
                               the_row_titles=titles,
                               the_data=contents,)
    except ConnectionError as err:
        print('Is your database switched on? Error: ', str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Error: ', str(err))
    except SQLErrors as err:
        print('Is your query Correct? Error :', str(err))
    except Exception as err:
        print('Something went wrong:', str(err))
    return 'Error'

if __name__ == '__main__':
    app.run(debug=True)
