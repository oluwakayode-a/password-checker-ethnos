from django.contrib import admin
from .models import PasswordCheckResult, Task
# Register your models here.

admin.site.register(PasswordCheckResult)
admin.site.register(Task)