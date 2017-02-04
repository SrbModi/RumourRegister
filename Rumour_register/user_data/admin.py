from django.contrib import admin
from .models import *

class user_dataAdmin(admin.ModelAdmin):
	list_display=["user","village","city","state","PO","email","Desi","Mobile"]

admin.site.register(user_data,user_dataAdmin)

class add_dataAdmin(admin.ModelAdmin):
	list_display=["noi","email","Mobile","flag"]

admin.site.register(add_data,add_dataAdmin)
# Register your models here.
