import random
from flask import Flask

app = Flask(__name__)


@app.route("/rand")
def rand():
    val = random()  # または random()

    # 値に応じたラベルの判定（※閾値の条件は課題の指定に合わせてください）
    if val < 0.3:
        label = "smaller"
    elif val <= 0.7:
        label = "medium"
    else:
        label = "larger"

    # フォーマットに合わせて返却
    return f"r={val:.3f} {label}"