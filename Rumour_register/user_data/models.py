from __future__ import unicode_literals

from django.db import models

class user_data(models.Model):
	user=models.CharField(primary_key=True,max_length=120)
	address=models.CharField(max_length=200,null=True,blank=True)
	village=models.CharField(max_length=120,null=True,blank=True)
	email=models.CharField(max_length=120,null=True,blank=True)
	Desi=models.CharField(max_length=100,null=True,blank=True)
	PO=models.CharField(max_length=100,null=True,blank=True)
	Mobile=models.DecimalField(max_digits=10,decimal_places=0)
	city=models.CharField(max_length=100,null=True,blank=True)
	state=models.CharField(max_length=100,null=True,blank=True)
# Create your models here.
