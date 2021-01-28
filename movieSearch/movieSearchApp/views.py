from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
# Create your views here.
import json,os
import urllib.request


BASE_DIR = Path(__file__).resolve().parent.parent
secretJson = os.path.join(BASE_DIR, 'secrets.json')
def index(request):
    return render(request,'movieSearchApp/index.html');

def searchMovie(request):
    secret_file = json.loads(open(secretJson).read())
    client_id = secret_file['CLIENT_ID']
    client_secret = secret_file['CLIENT_SECRET']
    q = request.GET.get('input-movie')

    encText = urllib.parse.quote("{}".format(q))
    url = "https://openapi.naver.com/v1/search/movie?query=" + encText  # json 결과
    movie_api_request = urllib.request.Request(url)
    movie_api_request.add_header("X-Naver-Client-Id", client_id)
    movie_api_request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(movie_api_request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        result = json.loads(response_body)
        movies = result.get('items')
        for movie in movies:
            replaceActor=movie['actor']
            movie['actor']=replaceActor.replace("|",",")
            replaceDirector=movie['director']
            movie['director']=replaceDirector.replace("|","")
        content = {
            'movies': movies
        }
        return render(request, 'movieSearchApp/searchMovie.html', content)


    return ("실패")