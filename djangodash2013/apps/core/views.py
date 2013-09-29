from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from core.utils import get_facebook_friends
from django.shortcuts import resolve_url


def main(request, template=u'main.html'):
    if request.user.is_authenticated():
        friends = get_facebook_friends(request)
        friends_by_sex = dict()
        friends_by_sex[u'male'] = len([1 for friend in friends if friend['sex'] == u'male']) * 100.0 / len(friends)
        friends_by_sex[u'female'] = len([1 for friend in friends if friend['sex'] == u'female']) * 100.0 / len(friends)
    else:
        friends_by_sex = dict()
    context = dict(
        friends_by_sex=friends_by_sex
    )
    return render(request, template, context)