from django.contrib import admin
from .models import *

class forgot_dataAdmin(admin.ModelAdmin):
	list_display=["user","email","otp","flag"]

admin.site.register(forgot_data,forgot_dataAdmin)
# Register your models here.
