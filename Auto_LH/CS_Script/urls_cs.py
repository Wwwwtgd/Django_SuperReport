from django.urls import path
from Auto_LH.CS_Script import views_cs
from Auto_LH import views


urlpatterns = [
    path("", views.cs, name="cs"),
    path('download_base_excel/', views_cs.download_base_excel, name='download_base_excel'),
    path('download_docx_files/', views_cs.download_docx_files, name='download_docx_files'),
]