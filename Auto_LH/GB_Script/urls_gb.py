from django.urls import path
from Auto_LH.GB_Script import views_gb
from Auto_LH import views


urlpatterns = [
    path("", views.gb, name="gb"),
    path('get_form_data/', views_gb.get_form_data, name='get_form_data'),
    path('download_base_excel/', views_gb.download_base_excel, name='download_base_excel'),
    path('download_docx_files/', views_gb.download_docx_files, name='download_docx_files'),
]