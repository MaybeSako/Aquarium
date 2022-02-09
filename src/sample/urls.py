from django.urls import re_path
from django.contrib.auth import views as auth_views
from sample import views

app_name = 'sample'
urlpatterns = [
    re_path('signup/', views.Signup.as_view(), name='signup'), 
    re_path('login/', views.Login.as_view(), name='login'),
    re_path('logout/', views.Logout.as_view(), name='logout'), 
    re_path('', views.index, name='index'), # http://localhost:8000/sample/
]