"""Imports."""
from flask import Flask, render_template, request
from customfuncs import validate


app = Flask(__name__, static_folder='static')


@app.route('/', methods=['POST', 'GET'])
def form():
    """The main route function."""
    error = None

    if request.method == "POST":
        errors = validate(request.form['firstname'],
                          request.form['lastname'],
                          request.form['school'])
        if len(errors) > 0:
            error = " ".join(errors)

    return render_template('index.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
