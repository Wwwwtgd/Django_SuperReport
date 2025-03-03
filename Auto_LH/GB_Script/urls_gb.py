from django.urls import path
from Auto_LH.GB_Script import views_gb
from Auto_LH import views


urlpatterns = [
    path("", views.gb, name="gb"),
    path('get_form_gb_data/', views_gb.get_form_gb_data, name='get_form_gb_data'),
    path('download_gb_base_excel/', views_gb.download_gb_base_excel, name='download_gb_base_excel'),
]