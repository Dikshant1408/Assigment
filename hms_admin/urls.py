from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path('adminlanding/', views.adminlanding, name='adminlanding'),
    path('signup_success/', views.signup_success, name='signup_success'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('wrong_login_credentials/', views.wrong_login_credentials, name='wrong_login_credentials'),
    path('login/', views.login_view, name='login_view'),
    path('manage-doctors/', views.manage_doctors, name='manage_doctors'),
    path('register-doctor/', views.register_doctor, name='register_doctor'),
    path('doctor-registration/', views.doctor_registration, name='doctor_registration'),
    path('registration_successful/', views.registration_successful, name='registration_successful'),
    path('doctor-list-display/', views.doctor_list_display, name='doctor_list_display'),
    path('doctor-list/', views.doctor_list, name='doctor_list'),
    path('patients/', views.patient_list, name='patient_list'),
    path('queries/', views.view_queries, name='view_queries'),
]
