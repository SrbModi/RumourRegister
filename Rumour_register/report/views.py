from django.shortcuts import render
from django.http import HttpResponse
from .models import report
# Create your views here.


def add_repo(request):
	report.objects.create(no_cases=request.POST.get("no_cases"),
		symptoms=request.POST.get("symptoms"),
		prob_cause=request.POST.get("prob_cause"),
		doc_response=request.POST.get("doc_response"),
		cur_sit=request.POST.get("cur_sit"),
		#no_cases=request.POST.get("no_cases"),
		loc_response=request.POST.get("loc_response")
		)
	return render(request,".html") #add file name

#url(r'^check/(?P<id>\d+)/$', check)
def feed(request,id):
	for o in report.objects.all:
		str = '<div ><button type="button" class="btn btn-info" data-toggle="collapse"'
		str+= ' data-target="#'
		str+= str(o.serial)
		str+= '" style="padding: 0px;float:right; background-color: white;border: 0px;">'
		str+= '<img src="1.png" style="width:35px;height:35px;"/></button><h3>'
		str+= str(o.user_id)
		str+= '</h3><div id="'
		str+= str(o.serial)
		str+= '" class="collapse">'
		str+= '<h4>symptoms : </h4>'
		str+= str(o.symptoms)
		str+= '<h4>probable cause : </h4>'
		str+= str(o.prob_cause)
		str+= '<h4>doctor response : </h4>'
		str+= str(o.doc_response)
		str+= '<h4>relevent data : </h4>'
		str+= str(o.relevent) #dsds
		str+= '<h4>Local Response : </h4>'
		str+= str(o.loc_response)
		str+= '</div></div><hr>'

	return 

