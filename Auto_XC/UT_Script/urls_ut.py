from django.urls import path
from Auto_XC.UT_Script import views_ut
from Auto_XC import views

urlpatterns = [
    path("", views.ut, name="ut"),
    path('download_ut_base_excel/', views_ut.download_ut_base_excel, name='download_ut_base_excel'),
    path('download_ut_report/', views_ut.download_ut_report, name='download_ut_report'),
    path('update_ut_picture/', views_ut.update_ut_picture, name='update_ut_picture'),
    path('get_ut_list/', views_ut.get_ut_list, name='get_ut_list'),
    path('handle_ut_report_type/', views_ut.handle_ut_report_type, name='handle_ut_report_type'),
]
