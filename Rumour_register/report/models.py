from django.db import models

# Create your models here.

class report(models.Model):
	serial = models.AutoField(primary_key=True)
	user = models.CharField(max_length=30) 
	no_cases = models.SmallIntegerField(default =1)
	symptoms = models.CharField(max_length = 256)
	prob_cause = models.CharField(max_length=256)
	doc_response = models.CharField(max_length=256)
	cur_sit = models.CharField(max_length=256)
	# rel_reports = models.FileField(upload_to = './reports')  #check syntax
	loc_response = models.CharField(max_length=256)


# class check(models.Model):
# 	tags = ArrayField(models.SmallIntegerField(default = 0))
		