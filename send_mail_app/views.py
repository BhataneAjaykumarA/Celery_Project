from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_mail_func

# Create your views here.


def send_mail_to_all_view(request):
    print('in send_mail_to_all_view')
    send_mail_func.delay()
    return HttpResponse('This is send mail to all View')

