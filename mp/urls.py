#from django.contrib import admin
from django.urls import path
from . import views
#from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.homepage),
]

urlpatterns+=staticfiles_urlpatterns()