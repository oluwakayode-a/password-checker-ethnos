from django.db import models

# Create your models here.
class PasswordCheckResult(models.Model):
    hash_prefix = models.CharField(max_length=200)
    breach_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Breached {str(self.breach_count)} times"


class Task(models.Model):
    instance = models.ForeignKey(PasswordCheckResult, on_delete=models.CASCADE, null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)