import json

from celery.task import task

from api.models import Famous
from api.utils import parse_famous


@task(ignore_result=True)
def get_famous_task(user):
    year = user.date_of_birth.year
    month = user.date_of_birth.month
    day = user.date_of_birth.day

    count = Famous.objects.filter(user=user).count()

    if count == 0:
        people = parse_famous(year, month, day)
        Famous.objects.create(user=user, json=json.dumps(people))