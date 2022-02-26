from django.urls import re_path, path
from asset import views

app_name = 'asset'
urlpatterns = [
    re_path('create/', views.AssetCreateView.as_view(), name='asset_create'),
    re_path('create/complete/', views.AssetCreateCompleteView.as_view(), name='asset_create_complete'),
    re_path('list/', views.AssetListView.as_view(), name='asset_list'),
    re_path('test/', views.index, name='asset_index'),
    path('detail/<uuid:pk>/', views.AssetDetailView.as_view(), name='asset_detail'),  #re_pathだとうまくできない
]