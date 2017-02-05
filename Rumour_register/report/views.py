from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage,get_connection
from django.core.mail.backends.smtp import EmailBackend
from django.views.decorators.csrf import csrf_exempt
import requests
from django.contrib.auth.models import User
from user_data.models import *
# Create your views here.
@csrf_exempt
@login_required
def add_repo(request):
	response={}
	if request.method=="POST":
		try:
			user_row= user_data.objects.get(user=str(request.user))
			city=str(user_row.city)
			print city
			name=str(user_row.name)
			print name
			mobile_user=str(user_row.Mobile)
			print mobile_user
			email_user=str(user_row.email)
			print email_user
			address=str(user_row.address)
			print address
			desi=str(user_row.Desi)
			print desi
			mo_row=user_data.objects.get(Desi='MO',city=str(city))
			email=str(mo_row.email)
			print email
			mobile=str(mo_row.Mobile)
			print mobile
			response["success"]=True
			no_cases=int(request.POST.get("no_cases"))
			print no_cases
			symptoms=str(request.POST.get("symptoms"))
			print symptoms
			prob_cause=str(request.POST.get("prob_cause"))
			print prob_cause
			doc_response=str(request.POST.get("doc_response"))
			print doc_response
			cur_sit=str(request.POST.get("cur_sit"))
			print cur_sit
			loc_response=str(request.POST.get("loc_response"))
			print loc_response
			report.objects.create(no_cases=no_cases,symptoms=symptoms,prob_cause=prob_cause,doc_response=doc_response,cur_sit=cur_sit,loc_response=loc_response)
			body="""Hello
The following situation has been reported :

no of cases = %s

symptoms :
%s

probable cause :
%s

doctor response :
%s

current situations :
%s

local response :
%s

please take the appropriate action on the above reported case.

For more details you can contact 
name : %s
address : %s
designation/Type : %s
mobile: %s
email id : %s
with regards,
Team Rumour Register"""
			print body % (no_cases,symptoms,prob_cause,doc_response,cur_sit,loc_response,name,address,desi,mobile_user,email_user)
			backend=EmailBackend(host='smtp.gmail.com', port=587, username='arpitj938@gmail.com', password='ksdrxcafsezpopeu', use_tls=True, fail_silently=True)
			EmailMsg=EmailMessage("Rumour Register",body % (no_cases,symptoms,prob_cause,doc_response,cur_sit,loc_response,name,address,desi,mobile_user,email_user),'no-reply@gmail.com',['sourabh.modi14@gmail.com'] ,connection=backend)
			EmailMsg.send()
		except:
			response["success"]=False
		return HttpResponse(str("Thank you for your valuable feedback"))
	else:
		return render(request,"feed.html")

#url(r'^check/(?P<id>\d+)/$', check)
def feed(request):
	stra = ' '
	for o in report.objects.all():
		stra+= '<div ><button type="button" class="btn btn-info" data-toggle="collapse"'
		stra+= ' data-target="#a'
		stra+= str(o.serial)
		stra+= '" style="padding: 0px;float:right; background-color: white;border: 0px;">'
		stra+= '<img src="/static/assets1/img/team/1.png" style="width:35px;height:35px;"/></button><h3>no of cases :'
		stra+= str(o.no_cases)
		stra+= '</h3><div id="a'
		stra+= str(o.serial)
		stra+= '" class="collapse">'
		stra+= '<h4>symptoms : </h4>'
		stra+= str(o.symptoms)
		stra+= '<h4>probable cause : </h4>'
		stra+= str(o.prob_cause)
		stra+= '<h4>doctor response : </h4>'
		stra+= str(o.doc_response)
		# stra+= '<h4>relevent data : </h4>'
		# stra+= str(o.relevent) #dsds
		stra+= '<h4>Local Response : </h4>'
		stra+= str(o.loc_response)
		stra+= '</div></div><hr>'
	print str(stra)
	if request.user.is_authenticated():
		return render(request,'welcome1.html',{"x":stra})
	else:
		return render(request,'welcome.html',{"x":stra})

def about_us(request):
	if request.user.is_authenticated():
		return render(request,'about_us1.html')
	else:
		return render(request,'about_us.html')

def contact(request):
	if request.user.is_authenticated():
		return render(request,'Contact1.html')
	else:
		return render(request,'Contact.html')

