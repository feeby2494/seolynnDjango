from distutils.command.config import LANG_EXT
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(default='korean')
    user = models.ForeignKey(User, on_delete=models.PROTECT)

class Collection(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    language = models.ForeignKey(Language, on_delete=models.PROTECT, default=1)
    

class Word(models.Model):
    name = models.CharField(max_length=255)
    language = models.ForeignKey(Language, on_delete=models.PROTECT, default=1)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, blank=True, null=True)

