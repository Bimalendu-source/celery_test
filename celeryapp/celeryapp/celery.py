from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from datetime import timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celeryapp.settings")

app = Celery("celeryapp")
app.conf.enable_utc = False

app.conf.update(timezone="Asia/Kolkata")

app.config_from_object(settings, namespace="CELERY")

app.conf.beat_schedule = {
    "run-every-5-seconds": {
        "task": "celery_app.tasks.call_api",
        "schedule": timedelta(seconds=5),
    },
}

app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
