from __future__ import unicode_literals

from django.db import models

class forgot_data(models.Model):
	forgot_id=models.AutoField(primary_key=True)
	user_id=models.CharField(max_length=120,blank=True,null=True)
	email=models.CharField(max_length=120,blank=True,null=True)
	otp=models.DecimalField(decimal_places=0,max_digits=6)
	flag=models.SmallIntegerField(default=0)

# Create your models here.
