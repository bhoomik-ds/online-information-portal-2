from django.urls import path
from . import views
from .views import job_list, result_list, notification_list, notification_detail, upcoming_job_detail, callletter_list, upcoming_job_list, quicklink_list

urlpatterns = [
    path('', views.home, name='home'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('contact/', views.contact, name='contact'),
    path('jobs/', job_list, name='job_list'),
    path('results/', result_list, name='result_list'),
    path('notifications/', notification_list, name='notification_list'),
    path('notification/<int:pk>/', notification_detail, name='notification_detail'),
    path('upcoming/<int:pk>/', upcoming_job_detail, name='upcoming_job_detail'),
    path('callletters/', callletter_list, name='callletter_list'),
    path('upcoming-jobs/', upcoming_job_list, name='upcoming_job_list'),
    path('quicklinks/', quicklink_list, name='quicklink_list'),
]
