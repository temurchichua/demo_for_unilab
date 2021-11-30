from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/temo")
def temos_github():
    return redirect("https://github.com/temurchichua")


@app.route("/alisa")
def alisas_github():
    return redirect("https://github.com/alisa-sanakoeva")

if __name__ == "__main__":
    app.run(debug=True)
