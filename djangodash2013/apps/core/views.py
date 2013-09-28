from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from core.utils import get_facebook_friends
from django.shortcuts import resolve_url


def main(request):
    friends = get_facebook_friends(request)
    return  HttpResponse()