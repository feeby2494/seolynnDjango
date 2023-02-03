from django.contrib import admin
from .models import WorkOrder, Project

# Register your models here.
admin.site.register(WorkOrder)
admin.site.register(Project)