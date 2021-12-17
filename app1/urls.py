from django.urls import path
from django.urls import URLPattern
from app1.views import *
app_name='app1'
urlpatterns=[path('hii/',hii,name='hii')]