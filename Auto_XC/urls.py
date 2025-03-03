from django.urls import path, include
from Auto_XC.UT_Script import urls_ut
from Auto_XC.MT_Script import urls_mt

urlpatterns = [
    path("UT/",  include(urls_ut)),
    path("MT/",  include(urls_mt)),
]