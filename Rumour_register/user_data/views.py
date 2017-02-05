from django.shortcuts import render
from .models import *
from user_data.models import *
from forgot_password.models import *
import requests
from django import forms
from django.http import HttpResponseRedirect, HttpResponse,HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.views import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.core.mail import EmailMessage,get_connection
from django.core.mail.backends.smtp import EmailBackend
from login_data.models import  *

class UploadFileForm(forms.Form):
    file = forms.FileField()


@csrf_exempt
def signup(request):
	if request.user.is_authenticated():
		return render(request,'welcome.html')
	else:
		if request.method=="POST" :
			response={}
			try:
				name=str(request.POST.get("name"))
				print name
				address=request.POST.get("address")
				print address
				village=request.POST.get("village")
				print village
				email=str(request.POST.get("email"))
				print email
				Desi=str(request.POST.get("Desi"))
				print Desi
				PO=str(request.POST.get("PO"))
				password=str(request.POST.get("password"))
				print PO
				Mobile=request.POST.get("Mobile")
				print Mobile
				city=str(request.POST.get("city"))
				print city
				state=str(request.POST.get("state"))
				print state
				response["success"]=True
				login_data.objects.create(user=email,password=password)
				user_data.objects.create(user=email,name=name,email=email,village=village,Desi=Desi,PO=PO,Mobile=Mobile,city=city,state=state,address=address)
				forgot_data.objects.create(user=email,otp=int(0))
				User.objects.create_user(
				username=email,
				password=password,
				email=email,
				)
			except:
				response["success"]=False
			return HttpResponse(str(response))
		else:
			return render (request,'detail.html')

@login_required
@csrf_exempt
def add(request):
	if request.method=="POST" :
		check=str(request.POST.get("check"))
		print check
		response={}
		if check!=None:	
			try:
				noi=str(request.POST.get("noi"))
				print noi
				email=str(request.POST.get("email"))
				print email
				Mobile=str(request.POST.get("Mobile"))
				print Mobile
				add_data.objects.create(noi=noi,Mobile=Mobile,email=email,flag=1)
				response["success"]=True
				body="""Hello
you have been register for Rumour Register 
kindly complete step 2 
http://127.0.0.1:8000/register/
with regards,
Team Rumour Register
with regards,
Team Rumour Register"""
				# print body % ("no_cases",'symptoms','prob_cause','doc_response','cur_sit','loc_response')
				backend=EmailBackend(host='smtp.gmail.com', port=587, username='arpitj938@gmail.com', password='ksdrxcafsezpopeu', use_tls=True, fail_silently=True)
				EmailMsg=EmailMessage("Rumour Register",body,'no-reply@gmail.com',[email] ,connection=backend)
				EmailMsg.send()
				print str(email)
				response["success"]=True
			except:
				response["success"]=False
			# response["message"]="roll no already register"
			return HttpResponse(str(response))
		else:
			form = UploadFileForm(request.POST,
                  request.FILES)

	        if form.is_valid():
	            request.FILES['file'].save_to_database(
                model=add_data,
                mapdict=['noi', 'email', 'Mobile'])
	            return HttpResponseRedirect("/send_mail/")

	        else:
	            return HttpResponseBadRequest()

	else:
		form = UploadFileForm()
		return render (request,'add.html',{'form': form})
@csrf_exempt
def send_mail(request):
	response={}
	try:
		for o in add_data.objects.filter(flag=0):
			print o.flag
			o.flag=1
			o.save()
			body="""Hello
you have been register for Rumour Register 
kindly complete step 2 
http://127.0.0.1:8000/register/
with regards,
Team Rumour Register"""
			print body % ("no_cases",'symptoms','prob_cause','doc_response','cur_sit','loc_response')
			backend=EmailBackend(host='smtp.gmail.com', port=587, username='arpitj938@gmail.com', password='ksdrxcafsezpopeu', use_tls=True, fail_silently=True)
			EmailMsg=EmailMessage("Rumour Register",body ,'no-reply@gmail.com',[o.email] ,connection=backend)
			EmailMsg.send()
		response["success"]=True
		response["message"]="email sent"
	except:
		response["success"]=False
		response["message"]="email not sent"

	print str(response)
	return HttpResponse(str(response))