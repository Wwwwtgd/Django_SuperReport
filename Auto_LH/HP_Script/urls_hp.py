from django.urls import path
from Auto_LH.HP_Script import views_hp
from Auto_LH import views


urlpatterns = [
    path("", views.hp, name="hp"),
    path('download_base_excel/', views_hp.download_base_excel, name='download_base_excel'),
    path('download_docx_files/', views_hp.download_docx_files, name='download_docx_files'),
]