from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from . forms import UserCreateForm, LoginForm

# # Create your views here.
def index(request):
    #とりあえず文字列を返す。
    return render(request, 'index.html')

# def login(request):
#     #とりあえず文字列を返す。
#     return render(request, 'login.html')

class Signup(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/sample/index')
        return render(request, 'signup.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return  render(request, 'signup.html', {'form': form,})

create_account = Signup.as_view()

class Login(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/sample/index')
        return render(request, 'login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form,})

account_login = Login.as_view()

class Logout(LogoutView):
    template_name = "sample/index.html"