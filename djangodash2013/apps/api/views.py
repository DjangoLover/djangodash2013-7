from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from core.utils import get_facebook_friends
from django.shortcuts import resolve_url
import json

from .utils import parse_famous, parse_events_by_date


def get_famous(request):
    if request.user.is_authenticated:
        year = 1986
        month = 1
        day = 12

        people = parse_famous(year, month, day)
    else:
        people = None

    return HttpResponse(json.dumps(people), mimetype="application/json")

def get_events(request):
    if request.user.is_authenticated:
        year = 1986
        month = 1
        day = 12

        events = parse_events_by_date(year, month, day)
    else:
        events = None

    return HttpResponse(json.dumps(events), mimetype="application/json")