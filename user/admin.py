from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Doctor)
admin.site.register(Userprofile)