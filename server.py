from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<username>")
def hello_world_username(username=None):
    return render_template("./index.html", name=username)
