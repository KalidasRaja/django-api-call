from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apiendpoint/', views.indexEndPoint, name='api')
]