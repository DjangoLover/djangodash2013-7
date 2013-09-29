import json
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from core.utils import get_friends_pics
from core.models import Mosaic


def main(request, template=u'main.html'):
    if request.user.is_authenticated():
        get_friends_pics(request)
    else:
        friends_by_sex = dict()
    context = dict()
    return render(request, template, context)


@login_required()
def is_mosaic_ready(request):
    try:
        mosaic = Mosaic.objects.get(user=request.user)
    except Mosaic.DoesNotExist:
        mosaic = None
    if mosaic:
        response = dict(url=mosaic.image.url)
    else:
        response = dict()
    return HttpResponse(json.dumps(response))