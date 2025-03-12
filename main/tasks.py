import hashlib
from typing import Union

from main.constants import BREACH_LIST
from main.models import PasswordCheckResult, Task
from celery import shared_task
from django.core.cache import cache
import random


@shared_task
def check_password(password: str, task_id: int) -> Union[bool, int]:

    password_cache = cache.get("password")

    if password_cache is not None:
        obj = dict(password_cache)

        
    safe = True

    if password in BREACH_LIST:
        safe = False

    hashed_password = hashlib.sha1(password.encode()).hexdigest()



    
    obj, created = PasswordCheckResult.objects.get_or_create(hash_prefix=hashed_password)

    breach_count = 0

    if not safe:
        obj.breach_count = random.randint(0, 15)
        obj.save()
        
        breach_count = obj.breach_count

    task = Task.objects.get(id=task_id)
    task.completed = True
    task.instance = obj

    task.save()

    cache.set("password", {'hash': hashed_password, 'count': breach_count}, 30 * 60 * 60 * 24)

    return safe, breach_count


@shared_task
def test_sentry_error():
    1 / 0