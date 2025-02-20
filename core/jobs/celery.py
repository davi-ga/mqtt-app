"""
Celery configuration for the core application.

This module sets up the Celery application, configures it to use Django settings,
and defines a periodic task schedule.
"""

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

current_domain = settings.ALLOWED_HOSTS[0] if settings.ALLOWED_HOSTS else "localhost"

# app.conf.beat_schedule = {
#     "illumination_send_every_minute": {
#         "task": "illumination_send",
#         "schedule": crontab(minute='*/1'),
#     },
#     "humidity_send_every_minute": {
#         "task": "humidity_send",
#         "schedule": crontab(minute='*/1'),
#     },
#     "water_level_send_every_minute": {
#         "task": "water_level_send",
#         "schedule": crontab(minute='*/1'),
#     },
#     "sound_send_every_minute": {
#         "task": "sound_send",
#         "schedule": crontab(minute='*/1'),
#     },
# }

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    """
    A simple debug task that prints the request information.

    This task is useful for debugging purposes to ensure that the Celery
    worker is receiving and processing tasks correctly.
    """

    print(f"Request: {self.request!r}")
