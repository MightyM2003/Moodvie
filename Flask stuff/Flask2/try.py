import urllib.request
import json
id=input("Enter id: ")
with urllib.request.urlopen("https://api.themoviedb.org/3/movie/" + str(id) + "?api_key=e2d785691fd6ba0b452c46148610dde4&language=en-US") as url:
    data = json.loads(url.read().decode())
    a = len(data["genres"])
    b = data["genres"]
    _string = ""
    for i in range(a):
        _string = _string+b[i]["name"]+" "
    print(_string)
with urllib.request.urlopen("https://api.themoviedb.org/3/movie/" + str(id) + "/keywords?api_key=e2d785691fd6ba0b452c46148610dde4") as url:
    data = json.loads(url.read().decode())
    c = (data["keywords"])
    _len=len(data["keywords"])
    _string2 = ""
    for i in range(_len):
        _string2 = _string2 + c[i]["name"]+ " "
    print(_string2)
with urllib.request.urlopen("https://api.themoviedb.org/3/movie/" + str(id) + "/credits?api_key=e2d785691fd6ba0b452c46148610dde4&language=en-US") as url:
    data = json.loads(url.read().decode())
    _len1=len(data["crew"])
    director=""
    for i in range(_len1):
        if data["crew"][i]["known_for_department"]=="Directing":
            director = director+data["crew"][i]["name"]
            break
    print(director)