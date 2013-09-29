from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Mosaic(models.Model):
    image = models.ImageField(upload_to=u'mosaics')
    user = models.ForeignKey(User)