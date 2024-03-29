from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[
    path("",indexapp,name='index'),
    path("report/",report,name='report'),
    path("deletee/<id>/",dele,name='delete'),
    path("updatee/<id>/",updatee,name='update'),
    path("login/",login,name="login"),
    path("register/",register,name='register'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()