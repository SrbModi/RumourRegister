from __future__ import unicode_literals

from django.db import models

class login_data(models.Model):
	login_id=models.AutoField(primary_key=True)
	user=models.CharField(max_length=120,blank=True,null=False,unique=True)
	password=models.CharField(max_length=120,blank=True,null=True)


# Create your models here.
