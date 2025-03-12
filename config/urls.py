
from django.contrib import admin
from django.urls import path, include
from main.tasks import test_sentry_error

def trigger_error(request):
    test_sentry_error.delay()
    division_by_zero = 1 / 0

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('sentry-debug/', trigger_error),   
]