from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.dbsparta

matrix = list(
    db.movies.find({"title": "매트릭스"}, {"_id": False, "rank": False, "title": False})
)
# print(matrix[0]["point"])

aMovie = db.movies.find_one({"title": "매트릭스"})
matrix_point = aMovie["point"]
# print(matrix_point)

all_movies = list(db.movies.find())
for movie in all_movies:
    if movie["point"] == matrix_point:
        print(movie["title"])

# all_movies = list(db.moives.find({"point": matrix_point}))

# for movie in all_movies:
#     print(movie["title"])
