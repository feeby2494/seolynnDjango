from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=200)

    def get_link(self):
        return 'https://' + self.link

class Application(Project):
    stack_used = models.TextField()
    desc = models.TextField()

    
    

class CaseStudy(Project):
    r_lang = models.BooleanField()
    python = models.BooleanField()
    short_desc = models.TextField()
