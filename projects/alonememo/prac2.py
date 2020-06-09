from pymongo import MongoClient
from bs4 import BeautifulSoup

import requests
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


client = MongoClient('localhost', 27017)
db = client.dbsparta


def parseUrl(target_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    data = requests.get(target_url, headers=headers)

    soup = BeautifulSoup(data.text, "html.parser")

    title = soup.select_one('meta[property="og:title"]')
    image = soup.select_one('meta[property="og:image"]')
    desc = soup.select_one('meta[property="og:description"]')
    print(title, image, desc)

    title_content = title['content']
    imgae_content = image['content']
    desc_content = desc['content']

    doc = {
        'title' : title_content,
        'image' : imgae_content,
        'desc' : desc_content
    }
    return doc

# HTML을 주는 부분


@app.route('/')
def home():
   return render_template('index.html')


@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기

    articles = list(db.articles.find({}, {'_id' : False}))
    
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result': 'success', 'msg': '겟', 'articles' : articles})

## API 역할을 하는 부분


@app.route('/memo', methods=['POST'])
def saving():
    # 1. 클라이언트로부터 데이터를 받기
    url_receive = request.form['url']
    comment_receive = request.form['comment']
    # 2. meta tag를 스크래핑하기
    doc_return = parseUrl(url_receive)
    doc_return['comment'] = comment_receive
    doc_return['url'] = url_receive
    print(doc_return)

    # 3. mongoDB에 데이터 넣기
    db.articles.insert_one(doc_return)

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
