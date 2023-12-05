from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_packages, name='hire_packages'),
    path(
        'hire_request/<int:hire_package_id>',
        views.create_hire_request, name='hire_request'),
    path(
        'hire_request_list/',
        views.hire_request_list, name='hire_request_list'),
]
