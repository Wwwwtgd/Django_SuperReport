from django.urls import path
from Auto_LH.HC_Script import views_hc
from Auto_LH import views


urlpatterns = [
    path("", views.hc, name="hc"),
    path('download_base_excel/', views_hc.download_base_excel, name='download_base_excel'),
    path('download_docx_files/', views_hc.download_docx_files, name='download_docx_files'),
]