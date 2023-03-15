from django.shortcuts import render


from django.views.generic.edit import FormView
from django.http import HttpResponse


#new Start 
from django.core.mail import send_mail
from .tasks import send_mail_task2

def indexView(request):
    send_mail_task2.delay()
    return HttpResponse('Sent mail')

from .tasks import test_func

def celery_test_view(request):
    print('in celery test view---')
    # test_func.delay()
    test_func.apply_async(countdown=10) # apply countdown
    print('after in test view----')
    return HttpResponse('Celery Test View')


