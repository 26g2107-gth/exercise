from random import choice, random

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello!"


@app.route("/rand")
def rand_route():
    r = random()

    if r < 0.3:  # 0.3 未満
        category = "smaller"
    elif r <= 0.7:  # 0.3 以上 0.7 以下 (0.7 を含む)
        category = "medium"
    else:  # 0.7 より大きい
        category = "larger"

    return f"r={r:.3f} {category}"


@app.route("/template")
def template():
    return render_template("template.html", greeting="hello", title="あいさつ")


@app.route("/template_list")
def template_list():
    students = []
    for n in range(1, 101):  # students に 2xG2001〜100 を追加
        students.append(f"2xG2{n:03d}")  # noqa: PERF401

    return render_template("template_list.html", students=students, title="学生番号リスト")


@app.route("/template_dict")
def template_dict():
    students = {}
    for n in range(1, 101):
        students[f"2xG2{n:03d}"] = choice(["A", "B", "C"])

    return render_template("template_dict.html", classes=["A", "C"], students=students, title="学生ごとのクラス分け")
