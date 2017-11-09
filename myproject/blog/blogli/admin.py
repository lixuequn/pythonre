from django.contrib import admin

# Register your models here.
from blogli.models import *
admin.site.register([Catagory, Tag, Blog, Comment])

