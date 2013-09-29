import os
import uuid
from django.conf import settings
import json

from celery.task import task


from api.models import Famous
from api.utils import parse_famous
import json

@task(ignore_result=True)
def get_famous_task(user):
    year = 1963
    month = 1
    day = 23

    count = Famous.objects.count()

    if count == 0:
        people = parse_famous(year, month, day)

        Famous.objects.create(user=user, json=people)
