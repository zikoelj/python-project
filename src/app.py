from flask import Flask

app = Flask(__name__)


def add_numbers(a, b):
    """Retourne la somme de a et b."""
    return a + b


@app.route("/")
def index():
    return "Hello, world!"


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return str(add_numbers(a, b))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
