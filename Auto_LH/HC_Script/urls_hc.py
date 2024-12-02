from django.urls import path
from Auto_LH.HC_Script import views_hc
from Auto_LH import views


urlpatterns = [
    path("", views.hc, name="hc"),

]