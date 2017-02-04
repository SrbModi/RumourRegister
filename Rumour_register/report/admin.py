from django.contrib import admin
from .models import report
# Register your models here.

class reportadmin(admin.ModelAdmin):
	list_display = ["no_cases","symptoms","prob_cause","doc_response","cur_sit","loc_response"]

# class checkadmin(admin.ModelAdmin):
# 	list_display = ["tags"]
		

admin.site.register(report,reportadmin)
# admin.site.register(check,checkadmin)