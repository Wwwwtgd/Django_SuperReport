from django.urls import path
from Auto_LH.HP_Script import views_hp
from Auto_LH import views


urlpatterns = [
    path("", views.hp, name="hp"),

]