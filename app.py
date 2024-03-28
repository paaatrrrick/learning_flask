from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

storage = []

@app.route('/add', methods=['POST'])
def post():
    formData = dict(request.form)
    storage.append(formData)
    return render_template('index.html', storage=storage)

@app.route('/')
def index():
    return render_template('index.html', storage=storage)

@app.route('/about')
def mike():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)