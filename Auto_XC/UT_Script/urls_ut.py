from django.urls import path
from Auto_XC.UT_Script import views_ut
from Auto_XC import views

urlpatterns = [
    path("", views.ut, name="ut"),
    path('download_base_excel/', views_ut.download_base_excel, name='download_base_excel'),
    path('download_report/', views_ut.download_report, name='download_report'),
    path('update_picture/', views_ut.update_picture, name='update_picture'),
    path('get_ut_list/', views_ut.get_ut_list, name='get_ut_list'),
]
