from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient("localhost", 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/", methods=["GET"])
def listing():

    return jsonify({"result": "success"})


## API 역할을 하는 부분
@app.route("/", methods=["POST"])
def saving():
    # 클라이언트로부터 데이터를 받는 부분

    # meta tag를 스크래핑 하는 부분
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    return jsonify({"result": "success"})


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)

