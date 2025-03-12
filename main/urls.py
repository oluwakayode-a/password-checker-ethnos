from django.urls import path
from .views import PasswordCheckView, CheckTaskStatus

urlpatterns = [
    path('check-password', PasswordCheckView.as_view()),
    path('task-status/<int:task_id>/', CheckTaskStatus.as_view())
]