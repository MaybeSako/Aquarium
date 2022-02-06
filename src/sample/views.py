from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #とりあえず文字列を返す。
    return render(request, 'index.html')

def login(request):
    #とりあえず文字列を返す。
    return render(request, 'login.html')

def explore_collections(request):
    #とりあえず文字列を返す。
    return render(request, 'explore-collections.html')
