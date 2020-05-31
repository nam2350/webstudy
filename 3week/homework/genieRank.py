from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.dbsparta

charts = list(db.geniecharts.find())

for chart in charts:
    print(chart["rank"], chart["title"], chart["artist"])
