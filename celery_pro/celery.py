# from __future__ import absolute_import,unicode_literals

# import os

# from celery import Celery

# os.environ.setdefault('DJANGO_SETTINGS_MODULE','celery_pro.settings')

# app = Celery('celery_pro')
# app.config_from_object('django.conf:settings',namespace='CELERY')

# app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))

###### ------------------------------------
from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
# from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_pro.settings')     # src.settings is settings path
app = Celery('celery_pro')                                                 # src is project name 
app.conf.enable_utc = False                                         # set False for timezone
app.conf.update(timezone = 'Aisa/Kolkata')                          # set indian timezone

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

## ----------------------- Celery Beat Settings --- for that start celery beat server -- celery -A <project_name> beat -l info
from celery.schedules import crontab                    # for scheduling task
app.conf.beat_schedule = {
    'send-mail-every-day-at-7-03':{                     # name
        'task':'send_mail_app.tasks.send_mail_func',    # add function name to execute on that time
        'schedule': crontab(hour=19, minute=3),         # add schedule time to execute celery beat and send to celery worker
    }

}