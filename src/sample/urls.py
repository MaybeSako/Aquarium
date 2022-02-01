from django.urls import re_path
from sample import views

app_name = 'sample'
urlpatterns = [
    re_path('login/', views.login, name='login'),
    re_path('', views.index, name='index'),
]