from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from core.utils import get_facebook_friends
from django.shortcuts import resolve_url
import json
import random

from .utils import parse_famous, parse_events_by_date
from .models import Famous

from .utils import get_famous_utils
def get_famous(request):
    if request.user.is_authenticated:
        get_famous_utils(request)

        people = Famous.objects.filter(user=request.user)[0]
        people = people.json
        print people
        if people:
            people = json.loads(people)
            people = [get_random(people), get_random(people), get_random(people), get_random(people)]
    else:
        people = None

    return HttpResponse(json.dumps(people), mimetype="application/json")


def get_random(people):
    return people.pop((int(random.random() * len(people))))


def get_events(request):
    if request.user.is_authenticated:
        year = 1986
        month = 1
        day = 12

        events = parse_events_by_date(year, month, day)
    else:
        events = None

    return HttpResponse(json.dumps(events), mimetype="application/json")