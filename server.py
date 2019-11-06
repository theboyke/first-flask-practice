from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    # by default looks for index.html inside a templates folder in the same directory as this script.
    return render_template('index.html')


# @app.route("/another")
# def show():
#     return '<h1>Yo</h1>'


@app.route('/user/<username>')
def show(username):
    return f"Hi {username[5]}"


if __name__ == '__main__':
    app.run(debug=True)
