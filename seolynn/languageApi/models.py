from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Word(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.PROTECT)