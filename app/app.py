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

@app.route("/template_list") # ここから追加
def template_list():
    students = [] # 学生番号を入れるリスト（空っぽ）
    for n in range(1, 101): # students に 2xG2001〜100 を追加
        students.append(f"2xG2{n:03d}")
    return render_template("template_list.html", students=students,
title="学生番号リスト")