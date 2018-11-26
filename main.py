from flask import Flask, render_template, request
from customfuncs import validate

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods = ['POST', 'GET'])
def form():
    error = None
    if request.method == "POST":
        messages = validate(request.form['firstname'],
                            request.form['lastname'],
                            request.form['school'])
        if len(messages) > 0:
            error = " ".join(messages)

    return render_template('index.html', error = error)
if __name__ == '__main__':
    app.run(debug=True)
