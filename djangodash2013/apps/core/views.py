import json
from django.shortcuts import render, HttpResponse

from core.utils import get_friends_pics
from core.models import Mosaic
from api.utils import get_famous_utils

def main(request, template=u'main.html'):
    if request.user.is_authenticated():
        get_friends_pics(request)
        get_famous_utils(request)
    else:
        friends_by_sex = dict()
    context = dict()
    return render(request, template, context)


def is_mosaic_ready(request):
    if request.user.is_authenticated():
        try:
            mosaic = Mosaic.objects.get(user=request.user)
        except Mosaic.DoesNotExist:
            mosaic = None
        if mosaic:
            response = dict(url=mosaic.image.url)
        else:
            response = dict()
    else:
        response = dict()
    return HttpResponse(json.dumps(response))
