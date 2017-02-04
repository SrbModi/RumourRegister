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
def login_view(request):
	if request.user.is_authenticated():
		return render(request,'welcome.html')
	else:
		if request.method=="POST":
			response={}
			try:
				user=str(request.POST.get("user"))
				print str(user)
				password=str(request.POST.get("password"))
				print str(password)
				response["success"]=True
				if login_data.objects.filter(user=user).filter(password=password):
					user = authenticate(username=user, password=password)
					if user is not None:
						login(request, user)
						response["message"]="Welcome to Code NIT"
				else:
					response["message"]="user_id or password not matched"

			except:
				response["success"]=False
				response["message"]="user id and password not get"

			print str(response)
			return HttpResponseRedirect('')

		else:
			# return HttpResponseRedirect('/')
			return render(request,'login.html')

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')





