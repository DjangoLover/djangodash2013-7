from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from core.utils import get_friends_pics


def main(request, template=u'main.html'):
    if request.user.is_authenticated():
        get_friends_pics(request)
    else:
        friends_by_sex = dict()
    context = dict()
    return render(request, template, context)