from django.contrib import admin
from django.urls import path

from .views import indexView, celery_test_view

urlpatterns = [
    path('index',indexView,name='index'),
    path('celery-test',celery_test_view,name='celery-test'),

]