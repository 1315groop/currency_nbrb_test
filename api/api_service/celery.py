from __future__ import absolute_import
from __future__ import unicode_literals

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_service.settings")

app = Celery("api")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
