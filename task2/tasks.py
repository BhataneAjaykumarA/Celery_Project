
#new task for mail
from django.core.mail import send_mail
from celery import shared_task
  
@shared_task
def send_mail_task2():
    print('Start-Task')
    send_mail(
        'Subject Celery2',
        'MSG Celery2',
        'ajaybhatanetemp@gmail.com',
        ['ajaykumarbhatane@gmail.com'],
        fail_silently=False
    )
    print('End-Task')
    return f'Task mail Sent'