from django.urls import path
from django.urls import URLPattern
from app2.views import *
app_name='app2'
urlpatterns=[path('hello/',hello,name='hello')]