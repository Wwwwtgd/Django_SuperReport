from django.urls import path
from Auto_XC.MT_Script import views_mt
from Auto_XC import views

urlpatterns = [
    path("", views.mt, name="mt"),
    path('download_mt_base_excel/', views_mt.download_mt_base_excel, name='download_mt_base_excel'),
    path('download_mt_report/', views_mt.download_mt_report, name='download_mt_report'),
    path('update_mt_picture/', views_mt.update_mt_picture, name='update_mt_picture'),
    path('get_mt_list/', views_mt.get_mt_list, name='get_mt_list'),
]