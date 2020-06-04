from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

## HTML을 주는 부분
@app.route("/")
def home():
    return render_template("index.html")


## API 역할을 하는 부분
# @app.route('/test', methods=['POST'])
# def test_post():
#    title_receive = request.form['title_give']
#    title_receive2 = request.form
#    print(title_receive)
#    print(title_receive2)
#    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})


@app.route("/test", methods=["GET"])
def test_get():
    title_receive = request.args.get("title_give")
    title_receive2 = request.args
    print(title_receive)
    print(title_receive2)
    return jsonify({"result": "success", "msg": "이 요청은 GET!"})


if __name__ == "__main__":
    app.run("127.0.0.1", port=5000, debug=True)
