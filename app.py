from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

storage = []

@app.route('/predict', methods=['POST'])
def post():
    formData = dict(request.form)
    storage.append(formData)
    print(storage)

    return render_template('index.html')




    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def mike():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)