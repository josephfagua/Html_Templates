from flask import render_template, Flask,url_for

app = Flask(__name__)


@app.route('/', methods=['Get'])
def navbar_styles():
    return render_template('testing.html', value=2)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
