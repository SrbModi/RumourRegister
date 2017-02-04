from django.contrib import admin
from .models import *

class login_dataAdmin(admin.ModelAdmin):
	list_display=["user","password"]

admin.site.register(login_data,login_dataAdmin)

# Register your models here.
