from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Candidate)
admin.site.register(models.Employee)