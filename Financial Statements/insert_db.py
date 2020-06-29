import json

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient("localhost", 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

with open('dart_name_code.json') as json_file:
    json_data = json.load(json_file)

    corp_data = json_data["result"]["list"]
    # print(corp_name)
    
    for corp_codes_names in corp_data:
        corp_name = corp_codes_names["corp_name"]
        corp_code = corp_codes_names["corp_code"]
        modify_date = corp_codes_names["modify_date"]

        doc = {"name" : corp_name, "code" : corp_code, "modify_date" : modify_date}
        db.corp_data.insert_one(doc)
        