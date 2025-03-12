import os

from celery import Celery, signals
import sentry_sdk
from django.conf import settings
from sentry_sdk.integrations.celery import CeleryIntegration

# this code copied from manage.py
# set the default Django settings module for the 'celery' app.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

sentry_sdk.init(
    dsn="https://439526e950dd3ccdbf7a1dfc0795caed@o4508964631871488.ingest.us.sentry.io/4508964741382144",  # Replace with your Sentry DSN
    integrations=[CeleryIntegration()],
)

# you can change the name here
app = Celery("app")

# read config from Django settings, the CELERY namespace would make celery
# config keys has `CELERY` prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# discover and load tasks.py from from all registered Django apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@signals.celeryd_init.connect
def init_sentry(**_kwargs):
    sentry_sdk.init(...) 
