from django.urls import path
from .views import *

urlpatterns = [
    
    path('', home, name="home"),
    path('menu/', menu, name="menu"),
    path('about/', about, name="about"),
    path('book/', book, name="book"),
]
