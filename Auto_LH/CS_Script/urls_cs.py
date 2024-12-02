from django.urls import path
from Auto_LH.CS_Script import views_cs
from Auto_LH import views


urlpatterns = [
    path("", views.cs, name="cs"),

]