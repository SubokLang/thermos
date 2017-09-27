from flask import Flask
from flask import render_template
from flask import url_for
#import os

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    #port =  int(os.environ.get('PORT',5000))
    app.run(debug=True)