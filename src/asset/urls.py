from django.urls import re_path
from . import views
 
app_name = 'asset'
urlpatterns = [
    re_path('create/', views.AssetCreateView.as_view(), name='create'),
    re_path('complete/', views.AssetCreateCompleteView.as_view(), name='complete'),
    re_path('', views.index, name='index'),
]