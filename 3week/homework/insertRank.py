import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient


client = MongoClient("localhost", 27017)
db = client.dbsparta

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

data = requests.get(
    "https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1",
    headers=headers,
)

soup = BeautifulSoup(data.text, "html.parser")

genieCharts = soup.select("#body-content > div.newest-list > div > table > tbody > tr")

# 순위
# body-content > div.newest-list > div > table > tbody > tr > td.number

# 타이틀
# body-content > div.newest-list > div > table > tbody > tr > td.info > a.title.ellipsis

# 가수
# body-content > div.newest-list > div > table > tbody > tr > td.info > a.artist.ellipsis

for chart in genieCharts:
    rankText = chart.select_one("td.number").text.rstrip()
    rank = rankText.strip(" 상 승 " + " 하 강 " + " 유 지 " + " new " + " ")
    title = chart.select_one("td.info > a.title.ellipsis").text.lstrip()
    artist = chart.selecddt_one("td.info > a.artist.ellipsis").text
    # print(rank[:-2].rstrip(), title, artist)
    doc = {"rank": rank[:-2].rstrip(), "title": title, "artist": artist}
    db.geniecharts.insert_one(doc)
