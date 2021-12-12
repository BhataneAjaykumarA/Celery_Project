from django.shortcuts import render


#from django.views.generic.edit import FormView
from django.http import HttpResponse


#new Start 
from django.core.mail import send_mail
from .tasks import send_mail_task2

def indexView(request):
    send_mail_task2.delay()
    return HttpResponse('Sent mail')

