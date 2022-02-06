from django.urls import re_path
from sample import views

app_name = 'sample'
urlpatterns = [
    re_path('explore_collections', views.explore_collections, name='explore_collections'),
    re_path('', views.index, name='index'),
]