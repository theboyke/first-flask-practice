from flask import Flask, render_template
app = Flask(__name__)


@app.route("/<name>")
def index(name):
    name = name.upper()
    # by default looks for index.html inside a templates folder in the same directory as this script.
    signed_in = True
    return render_template('index.html', name=name, signed_in=signed_in)


# @app.route("/another")
# def show():
#     return '<h1>Yo</h1>'


@app.route('/user/<username>')
def show(username):
    return f"Hi {username[2]}"


@app.route('/')
def home():
    return 'This is the homescreen!'


if __name__ == '__main__':
    app.run(debug=True)
