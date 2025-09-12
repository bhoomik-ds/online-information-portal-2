from django.urls import path
from . import views
from .views import job_list, result_list, notification_list

urlpatterns = [
    path('', views.home, name='home'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('contact/', views.contact, name='contact'),
    path('jobs/', job_list, name='job_list'),
    path('results/', result_list, name='result_list'),
    path('notifications/', notification_list, name='notification_list'),
]
