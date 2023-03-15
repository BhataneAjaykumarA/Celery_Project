
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from celery import shared_task
# from django.conf import settings
from celery_pro import settings


@shared_task(bind=True)
def send_mail_func(self):
    print('in test_func file----')
    users = get_user_model().objects.all()      #all admin users
    print('count-->', users.count())
    for user in users:
        print('iterating user----')
        name = user.email
        to_email = 'ajaykumarbhatane@gmail.com' # user.email
        mail_subject = 'Celery Testing sub'
        print('name==>', name)
        message = 'Hi {}, this is celery testing msg'.format(name)
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email, ],
            fail_silently=False,
        )
        return  "Done..----"
    return 'Finished.....'