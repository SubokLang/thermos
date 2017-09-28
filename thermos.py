from flask import Flask
from flask import render_template
from flask import url_for
#import os

app = Flask(__name__)

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

@app.route('/add')
def add():
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