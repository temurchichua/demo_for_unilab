from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/temo")
def temos_github():
    print("ჩემი branch")
    return redirect("https://github.com/temurchichua")

@app.route("/nika")
def nikas_github():
    return redirect("https://github.com/nika-kvr")


if __name__ == "__main__":
    app.run(debug=True)
