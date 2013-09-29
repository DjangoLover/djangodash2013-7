from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Famous(models.Model):
    json = models.TextField(max_length=65000, null=True, blank=True)
    user = models.ForeignKey(User)