from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import Question
# Register your models here.
admin.site.register(Question)