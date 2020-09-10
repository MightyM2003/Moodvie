from flask import Flask, render_template, request, redirect, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import urllib.request
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = '3358a36bc2b3179feb0372717386ad2dfdee92c60f2de818c5ef7562a44d8c0a25bac26d7043eaf3110e37c0683e999672362ec5fd4e8cf74fcd9f01100cbcc7c61c02f0d9aaa1984c85828f4e7ac2c4fc22c7989ec49d7c289f4377022071d41e7e7d77d1e1a51d4c7b224b71cb682c91ff7d466c0869b9d077ed512c591b7f1c2677bc0a3674f2dece66fddf9314d6ef34bdfbe19a6244bb1169'


@app.route('/')
def index():
    with urllib.request.urlopen("https://api.themoviedb.org/3/movie/popular?api_key=e2d785691fd6ba0b452c46148610dde4&language=en-US&page=1") as url:
        data1 = json.loads(url.read().decode())
        data2 = data1["results"]
        popmov=[]
        linkpop=[]
        for i in range(20):
            # print(i)
            try:
                # print(data2[i])
                data3 = data2[i]
            except:
                continue
            try:
                print(data3["original_name"] + ":")
                if "/n" in data3["original_name"]:
                    strippedtitle=data3["original_name"].replace("/n", " ")
                    popmov.append(strippedtitle)
                else:
                    popmov.append(data3["original_name"])
            except:
                print(data3["original_title"] + ":")
                if "/n" in data3["original_title"]:
                    strippedtitle=data3["original_title"].replace("/n", " ")
                    popmov.append(strippedtitle)
                else:
                    popmov.append(data3["original_title"])
            linkpop.append(data3["id"])
            print(data3["overview"])
            print("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
            popmov.append("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))

    with urllib.request.urlopen("https://api.themoviedb.org/3/movie/top_rated?api_key=e2d785691fd6ba0b452c46148610dde4&language=en-US&page=1") as url:
        data1 = json.loads(url.read().decode())
        data2 = data1["results"]
        topmov=[]
        linkpop1 = []
        for i in range(20):
            # print(i)
            try:
                # print(data2[i])
                data3 = data2[i]
            except:
                continue
            try:
                print(data3["original_name"] + ":")
                topmov.append(data3["original_name"])
            except:
                print(data3["original_title"] + ":")
                topmov.append(data3["original_title"])
            linkpop1.append(data3["id"])
            print(data3["overview"])
            print("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
            topmov.append("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))

    with urllib.request.urlopen("https://api.themoviedb.org/3/movie/upcoming?api_key=e2d785691fd6ba0b452c46148610dde4&language=en-US&page=1") as url:
        data1 = json.loads(url.read().decode())
        data2 = data1["results"]
        upmov=[]
        linkpop2 = []
        for i in range(20):
            # print(i)
            try:
                # print(data2[i])
                data3 = data2[i]
            except:
                continue
            try:
                print(data3["original_name"] + ":")
                upmov.append(data3["original_name"])
            except:
                print(data3["original_title"] + ":")
                upmov.append(data3["original_title"])
            linkpop2.append(data3["id"])
            print(data3["overview"])
            print("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
            upmov.append("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
    return render_template('index.html', popmov=popmov, topmov=topmov, upmov=upmov,linkpop=linkpop, linkpop1=linkpop1, linkpop2=linkpop2)

@app.route('/process_name/', methods=['POST', 'GET'])
def process_name():
    type = request.form['cars']
    name = request.form['name']
    search = name.split()
    global searchreq
    searchreq = "+".join(search)
    a = '/process/1'
    return redirect('/process_name/type='+ type + '/page=1/query='+ searchreq)


@app.route('/process_name/type=<type>/page=<num>/query=<name>', methods = ['POST','GET'])
def process(num, type, name):
    global data
    global name1
    global poster
    global twd
    if type == "Person":
        with urllib.request.urlopen("https://api.themoviedb.org/3/search/person?sort_by=popularity.desc&api_key=e2d785691fd6ba0b452c46148610dde4&query=" + name + "&page=" + str(num) + "&sort_by=popularity.desc") as url:
            print("https://api.themoviedb.org/3/search/person?sort_by=popularity.desc&api_key=e2d785691fd6ba0b452c46148610dde4&query=" + name + "&page=1" + "&sort_by=popularity.desc")
            display=[]
            data = json.loads(url.read().decode())
            print(data)
            title = []
            posterlink = []
            id = []
            pages = data['total_pages']
            if data['total_results']<20:
                a=data['total_results']
            else:
                a=20
            data1 = data['results']
            for i in range(a):
                data2 = data1[i]
                id.append(data2['id'])
                knownfor = data2['known_for']
                print("Known for:")
                for i in range(3):
                    try:
                        # print(i)
                        twd = (knownfor[i])
                        # print(str(i) + " " + str(twd))
                        # stuff=""
                        try:
                            # stuff += (twd['original_name'])
                            title.append(twd['original_name'])
                            if twd['poster_path'] == "None":
                                posterlink.append("https://i.ibb.co/1n24z5s/Moodvie.png")
                            else:
                                posterlink.append("https://image.tmdb.org/t/p/w500/" + str(twd['poster_path']))
                            print(twd['original_name'] + " " + "https://image.tmdb.org/t/p/w500/" + str(
                                twd['poster_path']))
                        except:
                            title.append(twd['original_title'])
                            if twd['poster_path'] == "None":
                                posterlink.append("https://i.ibb.co/1n24z5s/Moodvie.png")
                            else:
                                posterlink.append("https://image.tmdb.org/t/p/w500/" + str(twd['poster_path']))
                            # stuff += (twd['original_title'])
                            print(twd['original_title'] + " " + "https://image.tmdb.org/t/p/w500/" + str(
                                twd['poster_path']))
                    except:
                        print("")
                # print(data1)
                # print(data2
                print(data2['name'])
                name1 = data2['name']
                poster = "https://image.tmdb.org/t/p/w500/" + str(data2['profile_path'])
                print("https://image.tmdb.org/t/p/w500/" + str(data2['profile_path']))
                display.append(name1)
                display.append("https://image.tmdb.org/t/p/w500/" + str(data2['profile_path']))
            print(display)
            return render_template('new.html', display=display, title=title, posterlink=posterlink, id=id, name=name, pages=pages, type=type, a=a)
    elif type == "Movie":
        display = []
        id=[]
        with urllib.request.urlopen("https://api.themoviedb.org/3/search/movie?sort_by=popularity.desc&&include_adult=false&api_key=e2d785691fd6ba0b452c46148610dde4&language=en-US&page=" + str(num) + "&query=" + name) as url:
            data = json.loads(url.read().decode())
            data1=data['results']
            pages = data['total_pages']
            if data['total_results']<20:
                a=data['total_results']
            else:
                a=20
            for i in range(a):
                try:
                    # print(data2[i])
                    data3 = data1[i]
                except:
                    continue
                try:
                    display.append(data3["original_name"] + ":")
                except:
                    display.append(data3["original_title"] + ":")
                id.append(data3["id"])
                display.append("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
            return render_template('new.html', display=display, id=id, type=type, pages=pages, name=name, a=a)
    elif type == "TV":
        display = []
        id=[]
        with urllib.request.urlopen("https://api.themoviedb.org/3/search/tv?sort_by=popularity.desc&api_key=e2d785691fd6ba0b452c46148610dde4&language=en-US&page=" + str(num) + "&include_adult=false&query=" + name) as url:
            data = json.loads(url.read().decode())
            data1=data['results']
            pages = data['total_pages']
            if data['total_results']<20:
                a=data['total_results']
            else:
                a=20
            for i in range(a):
                try:
                    # print(data2[i])
                    data3 = data1[i]
                except:
                    continue
                try:
                    display.append(data3["original_name"] + ":")
                except:
                    display.append(data3["original_title"] + ":")
                id.append(data3["id"])
                display.append("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
            return render_template('new.html', display=display, id=id, type=type, pages=pages, name=name, a=a)
    elif type == "All":
        with urllib.request.urlopen("https://api.themoviedb.org/3/search/person?sort_by=popularity.desc&api_key=e2d785691fd6ba0b452c46148610dde4&query=" + name + "&page=" + str(num) + "&sort_by=popularity.desc") as url:
            print("https://api.themoviedb.org/3/search/person?sort_by=popularity.desc&api_key=e2d785691fd6ba0b452c46148610dde4&query=" + name + "&page=1" + "&sort_by=popularity.desc")
            display_person=[]
            data = json.loads(url.read().decode())
            print(data)
            title = []
            posterlink = []
            id_person = []
            pages = data['total_pages']
            if data['total_results']<20:
                a_P=data['total_results']
            else:
                a_P=20
            data1 = data['results']
            for i in range(a_P):
                data2 = data1[i]
                id_person.append(data2['id'])
                knownfor = data2['known_for']
                print("Known for:")
                for i in range(3):
                    try:
                        # print(i)
                        twd = (knownfor[i])
                        # print(str(i) + " " + str(twd))
                        # stuff=""
                        try:
                            # stuff += (twd['original_name'])
                            title.append(twd['original_name'])
                            if twd['poster_path'] == "None":
                                posterlink.append("https://i.ibb.co/1n24z5s/Moodvie.png")
                            else:
                                posterlink.append("https://image.tmdb.org/t/p/w500/" + str(twd['poster_path']))
                            print(twd['original_name'] + " " + "https://image.tmdb.org/t/p/w500/" + str(
                                twd['poster_path']))
                        except:
                            title.append(twd['original_title'])
                            if twd['poster_path'] == "None":
                                posterlink.append("https://i.ibb.co/1n24z5s/Moodvie.png")
                            else:
                                posterlink.append("https://image.tmdb.org/t/p/w500/" + str(twd['poster_path']))
                            # stuff += (twd['original_title'])
                            print(twd['original_title'] + " " + "https://image.tmdb.org/t/p/w500/" + str(
                                twd['poster_path']))
                    except:
                        print("")
                # print(data1)
                # print(data2
                print(data2['name'])
                name1 = data2['name']
                poster = "https://image.tmdb.org/t/p/w500/" + str(data2['profile_path'])
                print("https://image.tmdb.org/t/p/w500/" + str(data2['profile_path']))
                display_person.append(name1)
                display_person.append("https://image.tmdb.org/t/p/w500/" + str(data2['profile_path']))
            print(display_person)

        display_TV = []
        id_TV = []
        with urllib.request.urlopen(
                "https://api.themoviedb.org/3/search/tv?sort_by=popularity.desc&api_key=e2d785691fd6ba0b452c46148610dde4&language=en-US&page=" + str(
                        num) + "&include_adult=false&query=" + name) as url:
            data = json.loads(url.read().decode())
            data1 = data['results']
            pages = data['total_pages']
            if data['total_results'] < 20:
                a_T = data['total_results']
            else:
                a_T = 20
            for i in range(a_T):
                try:
                    # print(data2[i])
                    data3 = data1[i]
                except:
                    continue
                try:
                    display_TV.append(data3["original_name"] + ":")
                except:
                    display_TV.append(data3["original_title"] + ":")
                id_TV.append(data3["id"])
                display_TV.append("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
        display_Movie = []
        id_Movie = []
        with urllib.request.urlopen("https://api.themoviedb.org/3/search/movie?sort_by=popularity.desc&&include_adult=false&api_key=e2d785691fd6ba0b452c46148610dde4&language=en-US&page=" + str(num) + "&query=" + name) as url:
            data = json.loads(url.read().decode())
            data1=data['results']
            pages = data['total_pages']
            if data['total_results']<20:
                a_M=data['total_results']
            else:
                a_M=20
            for i in range(a_M):
                try:
                    # print(data2[i])
                    data3 = data1[i]
                except:
                    continue
                try:
                    display_Movie.append(data3["original_name"] + ":")
                except:
                    display_Movie.append(data3["original_title"] + ":")
                id_Movie.append(data3["id"])
                display_Movie.append("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
        if a_M > 4:
            a_M = 4
        if a_P > 4:
            a_P = 4
        if a_T > 4:
            a_T=4

        return render_template('Multi.html', display_Movie=display_Movie, id_Movie=id_Movie, display_TV=display_TV, id_TV=id_TV, display_person=display_person, id_person=id_person, name=name, a_M=a_M, a_P=a_P, a_T=a_T,)


    # elif type == 'All':
    #     search = name
    #     search = search.split()
    #     # print(search)
    #     searchreq = "+".join(search)
    #     # print(searchreq)
    #     with urllib.request.urlopen(
    #             "https://api.themoviedb.org/3/search/multi?sort_by=popularity.desc&api_key=e2d785691fd6ba0b452c46148610dde4&query=" + searchreq + "&page=1" + "&sort_by=popularity.desc") as url:
    #         # global data
    #         data = json.loads(url.read().decode())
    #         # print(data)
    #         if data["total_pages"] > 1:
    #             a = "True"
    #             # print(data['total_results'])
    #             # if a==False:
    #             # print(data)
    #             # print(data['total_results'])
    #             with urllib.request.urlopen(
    #                     "https://api.themoviedb.org/3/search/multi?sort_by=popularity.desc&api_key=e2d785691fd6ba0b452c46148610dde4&query=" + searchreq + "&page=1") as url:
    #                 data1 = json.loads(url.read().decode())
    #                 data2 = data1["results"]
    #                 display = []
    #                 for i in range(20):
    #                     # print(i)
    #                     try:
    #                         # print(data2[i])
    #                         data3 = data2[i]
    #                     except:
    #                         continue
    #                     try:
    #                         print(data3["original_name"] + ":")
    #                         display.append(data3["original_name"])
    #                         print(data3["overview"])
    #                         print("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
    #                         display.append("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
    #                     except:
    #                         try:
    #                             print(data3["original_title"] + ":")
    #                             display.append(data3["original_title"])
    #                             print(data3["overview"])
    #                             print("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
    #                             display.append("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
    #                         except:
    #                             print(data3["name"] + ":")
    #                             print("https://image.tmdb.org/t/p/w500/" + str(data3['profile_path']))
    #                             display.append("https://image.tmdb.org/t/p/w500/" + str(data3['profile_path']))
    #                 print(
    #                     "============================================================================================================================================================================")
    #                 print(display)
    #             # print("next level")
    #             # print(a)
    #             if a:
    #                 # print(data["total_results"])
    #                 for i in range(data["total_pages"] - 1):
    #                     with urllib.request.urlopen(
    #                             "https://api.themoviedb.org/3/search/multi?sort_by=popularity.desc&api_key=e2d785691fd6ba0b452c46148610dde4&query=" + searchreq + "&page=" + str(
    #                                 i + 2)) as url:
    #                         data1 = json.loads(url.read().decode())
    #                         # print(data1)
    #                         data2 = data1["results"]
    #                         # print(data2)
    #                         for i in range(12):
    #                             try:
    #                                 print(data2[i])
    #                                 data3 = data2[i]
    #                             except:
    #                                 continue
    #                             try:
    #                                 print(data3["original_name"] + ":")
    #                                 display.append(data3["original_name"])
    #                                 print(data3["overview"])
    #                                 print("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
    #                                 display.append("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
    #                             except:
    #                                 try:
    #                                     print(data3["name"] + ":")
    #                                     print("https://image.tmdb.org/t/p/w500/" + str(data3['profile_path']))
    #                                     display.append(data3["name"])
    #                                     display.append("https://image.tmdb.org/t/p/w500/" + str(data3['profile_path']))
    #
    #                                 except:
    #                                     print(data3["original_title"] + ":")
    #                                     display.append(data3["original_title"])
    #                                     print(data3["overview"])
    #                                     print("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
    #                                     display.append("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
    #                         print("dfjh skjdhf skdhfksjdhffksdjfhksf ifuhskdfhs df sdfkhskdfh sdf"
    #                               "sdfs idfush dkfhskdfhskdfh kshdf kshd fkshdfkj sdkfjh hsdkfhskdhffksdhfkshdf ksh fk s hdfkjsf===========================================================================")
    #                         print(display)
    #                 with urllib.request.urlopen(
    #                         "https://api.themoviedb.org/3/search/multi?sort_by=popularity.desc&api_key=e2d785691fd6ba0b452c46148610dde4&query=" + searchreq + "&page=" + str(
    #                             data["total_results"])) as url:
    #                     data = json.loads(url.read().decode())
    #                     data2 = data["results"]
    #                     sum = data["total_results"] - 1
    #                     sum2 = data["total_results"] - sum
    #                     for i in range(sum2):
    #                         # print(i)
    #                         try:
    #                             data3 = data2[i - 2]
    #                             print(data3["original_name"] + ":")
    #                             print(data3["overview"])
    #                             print("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
    #                         except:
    #                             print("No more results found")
    #             return render_template('movie.html', display=display)
    #         elif data["total_pages"] == 1:
    #             a = "False"
    #             # print(data['total_results'])
    #             # if a==False:
    #             # print(data)
    #             # print(data['total_results'])
    #             with urllib.request.urlopen(
    #                     "https://api.themoviedb.org/3/search/multi?sort_by=popularity.desc&api_key=e2d785691fd6ba0b452c46148610dde4&query=" + searchreq + "&page=1") as url:
    #                 data1 = json.loads(url.read().decode())
    #                 data2 = data1["results"]
    #                 display = []
    #                 idfirst = data2[0]
    #                 idfirst=idfirst["id"]
    #                 for i in range(20):
    #                     # print(i)
    #                     try:
    #                         # print(data2[i])
    #                         data3 = data2[i]
    #                     except:
    #                         continue
    #                     try:
    #                         print(data3["name"] + ":")
    #                         display.append(data3["name"])
    #                         print("https://image.tmdb.org/t/p/w500/" + str(data3['profile_path']))
    #                         display.append("https://image.tmdb.org/t/p/w500/" + str(data3['profile_path']))
    #                     except:
    #                         try:
    #                             print(data3["original_title"] + ":")
    #                             display.append(data3["original_title"])
    #                             print(data3["overview"])
    #                             print("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
    #                             display.append("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
    #                         except:
    #                             print(data3["original_name"] + ":")
    #                             display.append(data3["original_name"])
    #                             print(data3["overview"])
    #                             print("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
    #                             display.append("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
    #
    #                 print(
    #                     "============================================================================================================================================================================")
    #                 print(display)
    #                 # if len(display)<=10:
    #                 #     with urllib.request.urlopen(
    #                 #             "https://api.themoviedb.org/3/movie/"+str(idfirst)+"/similar?api_key=e2d785691fd6ba0b452c46148610dde4&language=en-US&page=1") as url:
    #                 #         data1 = json.loads(url.read().decode())
    #                 #         data2 = data1["results"]
    #                 #         display = []
    #                 #         idfirst = data2[0]
    #                 #         idfirst = idfirst["id"]
    #                 #         for i in range(20):
    #                 #             # print(i)
    #                 #             try:
    #                 #                 # print(data2[i])
    #                 #                 data3 = data2[i]
    #                 #             except:
    #                 #                 continue
    #                 #             try:
    #                 #                 print(data3["original_name"] + ":")
    #                 #                 display.append(data3["original_name"])
    #                 #             except:
    #                 #                 print(data3["original_title"] + ":")
    #                 #                 display.append(data3["original_title"])
    #                 #             print(data3["overview"])
    #                 #             print("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
    #                 #             display.append("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
    #             # print("next level")
    #             # print(a)
    #             if a:
    #                 # print(data["total_results"])
    #                 for i in range(data["total_pages"] - 1):
    #                     with urllib.request.urlopen(
    #                             "https://api.themoviedb.org/3/search/multi?sort_by=popularity.desc&api_key=e2d785691fd6ba0b452c46148610dde4&query=" + searchreq + "&page=" + str(
    #                                 i + 2)) as url:
    #                         data1 = json.loads(url.read().decode())
    #                         # print(data1)
    #                         data2 = data1["results"]
    #                         # print(data2)
    #                         for i in range(12):
    #                             try:
    #                                 print(data2[i])
    #                                 data3 = data2[i]
    #                             except:
    #                                 continue
    #                             try:
    #                                 print(data3["original_name"] + ":")
    #                                 display.append(data3["original_name"])
    #                             except:
    #                                 print(data3["original_title"] + ":")
    #                                 display.append(data3["original_title"])
    #                             print(data3["overview"])
    #                             print("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
    #                             display.append("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
    #                         print("dfjh skjdhf skdhfksjdhffksdjfhksf ifuhskdfhs df sdfkhskdfh sdf"
    #                               "sdfs idfush dkfhskdfhskdfh kshdf kshd fkshdfkj sdkfjh hsdkfhskdhffksdhfkshdf ksh fk s hdfkjsf===========================================================================")
    #                         print(display)
    #                 with urllib.request.urlopen(
    #                         "https://api.themoviedb.org/3/search/multi?sort_by=popularity.desc&api_key=e2d785691fd6ba0b452c46148610dde4&query=" + searchreq + "&page=" + str(
    #                             data["total_results"])) as url:
    #                     data = json.loads(url.read().decode())
    #                     data2 = data["results"]
    #                     sum = data["total_results"] - 1
    #                     sum2 = data["total_results"] - sum
    #                     for i in range(sum2):
    #                         # print(i)
    #                         try:
    #                             data3 = data2[i - 2]
    #                             print(data3["original_name"] + ":")
    #                             print(data3["overview"])
    #                             print("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
    #                         except:
    #                             print("No more results found")
    #             return render_template('movie.html', display=display)




@app.route('/Film/')
def Film():
    print("Recieved")
    movposter="https://image.tmdb.org/t/p/w500/" + twd['poster_path']
    overview=twd['overview']
    return render_template('new1.html', movposter=movposter, overview=overview)

@app.route('/Film/id/<int:id>')
def film_id(id):
    try:
        with urllib.request.urlopen("https://api.themoviedb.org/3/movie/"+ str(id) +"?api_key=e2d785691fd6ba0b452c46148610dde4&language=en-US") as url:
            data = json.loads(url.read().decode())
            print(data["adult"])
            if data["adult"]==True:
                stop=1
                print(stop)
                return render_template('Film.html', stop=stop)
            else:
                stop=2
                print(stop)
                try:
                    title = data["original_title"]
                except:
                    title = data["original_name"]
                poster = data["poster_path"]
                poster=("https://image.tmdb.org/t/p/w500/" + str(poster))
                overview = data["overview"]
                with urllib.request.urlopen("https://api.themoviedb.org/3/movie/" + str(id) + "/recommendations?api_key=e2d785691fd6ba0b452c46148610dde4&adult=false&language=en-US&page=1") as url:
                    data1 = json.loads(url.read().decode())
                    amount=data1["total_results"]
                    print(amount)
                    data2 = data1["results"]
                    display = []
                    linkpop = []
                    if amount==0:
                        pass
                    else:
                        for i in range(amount):
                            # print(i)
                            try:
                                # print(data2[i])
                                data3 = data2[i]
                            except:
                                continue
                            linkpop.append(data3["id"])
                            try:
                                print(data3["original_title"] + ":")
                                display.append(data3["original_title"])
                                print(data3["overview"])
                                print("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
                                display.append("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
                            except:
                                print(data3["original_name"] + ":")
                                display.append(data3["original_name"])
                                print(data3["overview"])
                                print("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
                                display.append("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
                return render_template('Film.html', title=title, poster=poster, overview=overview, display=display, linkpop=linkpop,stop=stop)
    except:
        stop = 1
        return render_template('Film.html', stop=stop)
@app.route('/People/id/<int:id>')
def people_id(id):
    try:
        with urllib.request.urlopen("https://api.themoviedb.org/3/person/" + str(id) + "?api_key=e2d785691fd6ba0b452c46148610dde4&language=en-US") as url:
            data = json.loads(url.read().decode())
            name=data["name"]
            description=data["biography"]
            search = name.split()
            image="https://image.tmdb.org/t/p/w500/" + str(data["profile_path"])
            searchreq = "+".join(search)
            print(searchreq)
    except:
        print("")
    with urllib.request.urlopen("https://api.themoviedb.org/3/search/person?sort_by=popularity.desc&api_key=e2d785691fd6ba0b452c46148610dde4&query=" + searchreq + "&page=1&sort_by=popularity.desc") as url:
        print("https://api.themoviedb.org/3/search/person?sort_by=popularity.desc&api_key=e2d785691fd6ba0b452c46148610dde4&query=" + searchreq + "&page=1" + "&sort_by=popularity.desc")
        data = json.loads(url.read().decode())
        print(data)
        title=[]
        posterlink=[]
        id=[]
        media=[]
        data1 = data['results']
        data2 = data1[0]
        knownfor = data2['known_for']
        print("Known for:")
        for i in range(3):
            try:
                # print(i)
                twd = (knownfor[i - 1])
                # print(str(i) + " " + str(twd))
                # stuff=""
                try:
                    # stuff += (twd['original_name'])
                    title.append(twd['original_name'])
                    posterlink.append("https://image.tmdb.org/t/p/w500/" + str(twd['poster_path']))
                    print(twd['original_name'] + " " + "https://image.tmdb.org/t/p/w500/" + str(twd['poster_path']))
                except:
                    title.append(twd['original_title'])
                    posterlink.append("https://image.tmdb.org/t/p/w500/" + str(twd['poster_path']))
                    # stuff += (twd['original_title'])
                    print(twd['original_title'] + " " + "https://image.tmdb.org/t/p/w500/" + str(twd['poster_path']))
            except:
                print("")
            media.append(twd['media_type'])
            id.append(twd['id'])
        print(id)
            # print(data1)
            # print(data2
        return render_template('Person.html', name=name, description=description, image=image, title=title, posterlink=posterlink, id=id,media=media)

@app.route('/TV/id/<int:id>')
def TV_id(id):
    with urllib.request.urlopen("https://api.themoviedb.org/3/tv/"+ str(id) +"?api_key=e2d785691fd6ba0b452c46148610dde4&language=en-US") as url:
        data = json.loads(url.read().decode())
        try:
            title = data["original_title"]
        except:
            title = data["original_name"]
        poster = data["poster_path"]
        poster=("https://image.tmdb.org/t/p/w500/" + str(poster))
        overview = data["overview"]
    with urllib.request.urlopen("https://api.themoviedb.org/3/tv/" + str(id) + "/recommendations?api_key=e2d785691fd6ba0b452c46148610dde4&adult=false&language=en-US&page=1") as url:
        data1 = json.loads(url.read().decode())
        amount=data1["total_results"]
        print(amount)
        data2 = data1["results"]
        display = []
        linkpop = []
        if amount==0:
            pass
        else:
            for i in range(amount):
                # print(i)
                try:
                    # print(data2[i])
                    data3 = data2[i]
                except:
                    continue
                linkpop.append(data3["id"])
                try:
                    print(data3["original_title"] + ":")
                    display.append(data3["original_title"])
                    print(data3["overview"])
                    print("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
                    display.append("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
                except:
                    print(data3["original_name"] + ":")
                    display.append(data3["original_name"])
                    print(data3["overview"])
                    print("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
                    display.append("https://image.tmdb.org/t/p/w500/" + str(data3["poster_path"]))
    return render_template('TV.html', title=title, poster=poster, overview=overview, display=display, linkpop=linkpop)
# @app.route('/demo1')
# def demoOne():
#
#     return render_template('demoOne.html', names=rows)

# @app.route('/api/addEntry', methods = ['POST'])
# def addEntry():
#     name =request.form['name']
#     age=request.form['age']
#     rows.append([name,age])
#     print("Recieved request to addEntry " + request.form["name"])
#     return jsonify({"success": True, "entries": rows})


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect('/')
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@app.route('/wtf')
def wtf():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect('/')
    return render_template('wtf.html', title='Register', form=form)

if __name__ == "__main__":
    app.run(debug=True)
