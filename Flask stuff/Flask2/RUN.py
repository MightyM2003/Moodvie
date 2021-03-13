from Flask2 import app, db, bcrypt, models
from flask_login import login_user, current_user, logout_user
# from flask_login import login_user, current_user, logout_user
import csv
import urllib.request
import json
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
print("sdjnskdjnf  sdkjfsdf sdfkjsndf sdfskjnfd sdfkjsnd v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v ")
print(current_user)
print("A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A ")
print("This file should work")

def add_movie(id, title):
    f = open("C:/Users\Rathod\PycharmProjects\Flask stuff\Flask2\demo.txt", "r")
    abc = f.read()
    with urllib.request.urlopen("https://api.themoviedb.org/3/movie/" + str(
            id) + "?api_key=e2d785691fd6ba0b452c46148610dde4&language=en-US") as url:
        data = json.loads(url.read().decode())
        a = len(data["genres"])
        b = data["genres"]
        _string = ""
        for i in range(a):
            _string = _string + b[i]["name"] + " "
    with urllib.request.urlopen("https://api.themoviedb.org/3/movie/" + str(
            id) + "/keywords?api_key=e2d785691fd6ba0b452c46148610dde4") as url:
        data = json.loads(url.read().decode())
        c = (data["keywords"])
        _len = len(data["keywords"])
        _string2 = ""
        for i in range(_len):
            _string2 = _string2 + c[i]["name"] + " "
    with urllib.request.urlopen("https://api.themoviedb.org/3/movie/" + str(
            id) + "/credits?api_key=e2d785691fd6ba0b452c46148610dde4&language=en-US") as url:
        data = json.loads(url.read().decode())
        _len1 = len(data["crew"])
        director = ""
        for i in range(_len1):
            if data["crew"][i]["known_for_department"] == "Directing":
                director = director + data["crew"][i]["name"]
                break
    with open('movie_dataset.csv', 'a', encoding="utf-8") as csvfile:
        fieldnames = [str(abc), "", str(_string), "", str(id), str(_string2), "", str(title), "", "", "", "", "", "",
                      "", "", "", "", str(title), "", "", "", "", str(director)]
        print(fieldnames)
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        df = pd.read_csv("""C:/Users\Rathod\PycharmProjects\Flask stuff\Flask2\movie_dataset.csv""")
    b = int(abc) + 1
    f = open("demo.txt", "w")
    f.write(str(b))
    f.close()


def get_title_from_index(index):
    df = pd.read_csv("""C:/Users\Rathod\PycharmProjects\Flask stuff\Flask2\movie_dataset.csv""")
    return df[df.index == index]["title"].values[0]


def get_index_from_title(title):
    df = pd.read_csv("""C:/Users\Rathod\PycharmProjects\Flask stuff\Flask2\movie_dataset.csv""")
    return df[df.title == title]["index"].values[0]
for i in range(18):
    print(i+1)
    df = pd.read_csv("""C:/Users\Rathod\PycharmProjects\Flask stuff\Flask2\movie_dataset.csv""")
    try:
        Movies = models.WatchLater.query.filter_by(User_id=i+1).all()
    except:
        continue
    amountWL = len(Movies)
    for i in range(amountWL):
        try:
            get_index_from_title(Movies[i].title)
        except IndexError:
            add_movie(Movies[i].id_movie, Movies[i].title)




def run(runfile):
    with open(runfile, "r") as rnf:
        exec(rnf.read())
run("C:/Users/Rathod/PycharmProjects/Flask stuff/run.py")