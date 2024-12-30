from django.urls import path, include
from Auto_XC.UT_Script import urls_ut

urlpatterns = [
    path("UT/",  include(urls_ut)),
]