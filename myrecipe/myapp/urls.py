from django.urls import path
from .views import *
urlpatterns=[
    path("",indexapp,name='index'),
    path("report/",report,name='report')
]