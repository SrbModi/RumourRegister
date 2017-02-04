from django.shortcuts import render
from .models import *
# from user_data.models import *
from forgot_password.models import *
from .models import *
import requests
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.views import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render_to_response
@csrf_exempt
def signup(request):
	if request.user.is_authenticated():
		return render(request,'welcome.html')
	else:
		if request.method=="POST" :
			response={}
			try:
				user=str(request.POST.get("user"))
				address=request.POST.get("address")
				village=request.POST.get("village")
				email=str(request.POST.get("email"))
				Desi=request.POST.get("Desi")
				PO=request.POST.get("PO")
				Mobile=request.POST.get("Mobile")
				city=request.POST.get("city")
				state=request.POST.get("state")
				response["success"]=True
				response["user_id"]=user_id
				login_data.objects.create(user_id=user_id,password=password)
				user_data.objects.create(user_id=user_id,user_name=user_name,roll_no=roll_no,sem=sem,email=email)
				forgot_data.objects.create(user_id=user_id,otp=int(0))
				User.objects.create_user(
				username=user_id,
				password=password,
				email=email,
				)
			except:
				response["success"]=False
				response["message"]="roll no already register"

			print(str(response))
			context={}
			context["user_name"]=user_name
			context["user_id"]=user_id
			context["email"]=email
			context["sem"]=sem
			context["roll_no"]=roll_no
			context["success"]=response["success"]
			return render (
				request,
				'ver_signup.html',context)
			#return HttpResponse(str(response))

		else:
			return render (request,'signup.html')

@csrf_exempt
def login_view(request):
	if request.user.is_authenticated():
		return render(request,'/')
	else:
		if request.method=="POST":
			response={}
			try:
				user_id=str(request.POST.get("user_id"))
				print str(user_id)
				password=str(request.POST.get("password"))
				print str(password)
				response["success"]=True
				if login_data.objects.filter(user_id=user_id).filter(password=password):
					user = authenticate(username=user_id, password=password)
					if user is not None:
						login(request, user)
						response["message"]="Welcome to Code NIT"
				else:
					response["message"]="user_id or password not matched"

			except:
				response["success"]=False
				response["message"]="user id and password not get"

			print str(response)
			return HttpResponse(str(response))

		else:
			# return HttpResponseRedirect('/')
			return render(request,'login.html')

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')





