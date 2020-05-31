# -*-coding: utf-8-*-
import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
data = requests.get(
    "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303",
    headers=headers,
)

soup = BeautifulSoup(data.text, "html.parser")

movies = soup.select("#old_content > table > tbody > tr")
for movie in movies:
    rank = movie.select_one("td.ac > img")
    a_tag = movie.select_one("td.title > div > a")
    point = movie.select_one("td.point")
    if a_tag is not None:
        print(rank.get("alt"), a_tag.text, point.text)
