from flask import Flask # Flask クラスの読込

app = Flask(__name__) # Flask クラスの実体を作成


@app.route("/") # / にアクセスされたときの処理
def index(): # を担当する関数 index()
    return "Hello!" # 文字列"Hello"を返す