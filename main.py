import flask
import requests
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)

@app.route('/')
def HomePage():
    return render_template("home.html")

@app.route('/hi', methods=['POST'])
def Hi():
    return "Hello!123"

@app.route('/mj')
def MJ():
    return render_template("mj.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=13500)
    # app.run(debug=True, host = "0.0.0.0", port=13500)
