"""Rumour_register URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from forgot_password.views import change_password,forgot_get_pass,forgot_ver_pass,welcome
from login_data.views import login_view
from user_data.views import signup,add,send_mail
from report.views import add_repo,feed

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',welcome),
    url(r'^forgot_password/$',forgot_get_pass),
    url(r'^verify_password/$',forgot_ver_pass),
    url(r'^change_password/$',change_password),
    url(r'^login/$',login_view),
    url(r'^register/$',signup),
    url(r'^add/$',add),
    url(r'^send_mail/$',send_mail),
    url(r'^add_repo/$',add_repo),
    url(r'^feed/$',feed),


]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
