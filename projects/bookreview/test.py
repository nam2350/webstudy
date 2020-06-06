from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index1.html')

## API 역할을 하는 부분

@app.route('/sparta', methods=['GET'])
def test_get():
    name = request.args.get('name')
    msg = request.args.get('msg')
    print('name : ' + name + 'msg : ' + msg)
    return jsonify({'name' : '하이', 'msg' : '반가워'})

@app.route('/abc', methods=['POST'])
def test_post():
    name = request.form['name']
    msg = request.form['msg']

    print('name : ' + name + 'msg : ' + msg)
    return jsonify({'name' : 'name', 'msg' : 'msg'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=2000, debug=True)