from django.contrib import admin
from django.urls import path

from .views import indexView

urlpatterns = [
    path('index',indexView,name='index')
]