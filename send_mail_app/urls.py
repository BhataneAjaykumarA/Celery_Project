from django.contrib import admin
from django.urls import path

from .views import send_mail_to_all_view

urlpatterns = [
    path('send-mail-all',send_mail_to_all_view,name='send-mail-all'),

]