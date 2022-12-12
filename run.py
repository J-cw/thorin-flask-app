import os
from flask import Flask, request, render_template

app = Flask(__name__)
# Creates instance of Flask class and storing in variable "app"


@app.route("/")
def index():
    return render_template("index.html")
# Decorator wraps functions, browse to root director function is triggered.


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
# Gets IP if exists else set to default value, same with port.
# Debug true to allow easier debugging durin dev
