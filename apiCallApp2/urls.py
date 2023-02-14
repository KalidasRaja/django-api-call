from django.urls import path
from . import views

urlpatterns = [
    path('apiendpoint', views.index, name='index'),
    path('api/', views.indexEndPoint, name='api'),
    path('client/', views.client, name='client'),

    path('search', views.search, name='search'),
    path('search-view', views.search_view, name='search_view'),
    path('', views.Makhzny, name='makhzny'),
    path('makhzny', views.Makhzny, name='makhzny'),
    path('minilager', views.MiniLager, name='minilager'),
    # path('api-search/', views.apisearch.as_view(), name='api-search'),
]