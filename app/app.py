from random import random

from flask import Flask, render_template # この行を修正

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello!"


@app.route("/rand")
def rand():
# チェックポイント 3 でこの関数は書き換わっているはず
    r = random()
    return f"{r=:.3f}"


@app.route("/template") # ここから追加
def template():
    return render_template("template.html", greeting="hello", title="あいさつ")