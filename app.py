import os
import sys
from flask import render_template, Flask

app = Flask(__name__)


@app.route('/')
def basic_navbar():
    return render_template('BasicNavbar.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
