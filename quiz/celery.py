from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')

app = Celery('recharge')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
  print('Request: {0!r}'.format(self.request))


# from celery.schedules import crontab
# app.conf.beat_schedule = {
    
# 'airtime': {
#         'task': 'recharge_airtime',
#         'schedule': 120.0,
#         # 'args': (16, 16)
#     },

#     'remove_airtime': {
#         'task': 'delete_airtime',
#         'schedule': 240.0,
#         # 'args': (16, 16)
#     },




# 'airtime_level': {
#         'task': 'recharge_airtime_level',
#         'schedule': 90.0,
#         # 'args': (16, 16)
#     },


#     # 'remove_airtime_level': {
#     #     'task': 'delete_airtime_level',
#     #     'schedule': 110.0,
#     #     # 'args': (16, 16)
#     # },   
    
#     # 'send_post_mail': {
#     #     'task': 'Schedule Mail',
#     #     'schedule': 240.0,
#     #     # 'args': (16, 16)
#     # },

#     'remove': {
#         'task': 'delete_game',
#         'schedule': 240.0,
#         # 'args': (16, 16)
#     },
#     'recharge': {
#         'task': 'recharge_taptap',
#         'schedule': 120.0,
#         # 'args': (16, 16)
#     },


#       'tap_sms': {
#         'task': 'taptap_sms',
#         'schedule': 60.0,
#         # 'args': (16, 16)
#     }


# }


