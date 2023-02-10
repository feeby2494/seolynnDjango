from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

class Application(Project):
    pass
    

class CaseStudy(Project):
    pass

