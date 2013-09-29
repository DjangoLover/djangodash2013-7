import os
import uuid
from django.conf import settings

from celery.task import task


from api.models import Famous
from api.utils import parse_famous


@task(ignore_result=True)
def get_famous(user):
    year = 1963
    month = 1
    day = 23

    json = parse_famous(year, month, day)

    Famous.objects.create(user=user, json=json)
