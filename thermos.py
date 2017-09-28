from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash

# from logging import DEBUG
#import os

app = Flask(__name__)
# app.logger.setLevel(DEBUG)

bookmarks = []
app.config['SECRET_KEY'] = "123456"

def store_bookmark(url):
    bookmarks.append(dict(
        url = url,
        user = "reindert",
        date = datetime.utcnow()
    ))

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def initials(self):
        return "{}. {}.".format(self.firstname[0], self.lastname[0])

@app.route('/')
@app.route('/index')
def index():
    titlevar = 'Title from view to template'
    userobj = User("John", "Doe")
    return render_template('index.html',title=titlevar,user=userobj)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url)
        # app.logger.debug('store url: ' + url)
        flash("Stored bookmark '{}'".format(url))
        return redirect(url_for('index'))
    return render_template('add.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    #port =  int(os.environ.get('PORT',5000))
    app.run(debug=True)