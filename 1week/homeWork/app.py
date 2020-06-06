from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.dbsparta


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/order", methods=["POST"])
def write_review():
    orderer = request.form["orderer"]
    amount = request.form["amount"]
    addr = request.form["addr"]
    phone = request.form["phone"]

    doc = {"orderer": orderer, "amount": amount, "addr": addr, "phone": phone}
    db.shopping.insert_one(doc)

    return jsonify({"result": "success", "msg": "이 요청은 POST!"})


@app.route("/order", methods=["GET"])
def read_reviews():
    shopping = list(db.shopping.find({}, {"_id": False}))
    return jsonify({"result": "success", "msg": "이 요청은 GET!", "shopping": shopping})


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
