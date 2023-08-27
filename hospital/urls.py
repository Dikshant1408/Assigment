from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='landing_page'),
    path('patient/', views.patient_landing, name='patient_landing'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('patient_register/', views.patient_register, name='patient_register'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('patient_login/', views.login_view, name='patient_login'),
    path('fix_appointment/', views.fix_appointment, name='fix_appointment'),
    path('appointment-success/', views.appointment_success, name='appointment_success'),
    path('doctor-login/', views.doctor_login, name='doctor_login'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('view-appointments/', views.view_appointments, name='view_appointments'),
    path('delete-appointment/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('write_prescription/', views.write_prescription, name='write_prescription'),
    path('prescription_saved/', views.prescription_saved, name='prescription_saved'),
    path('view-prescriptions/', views.view_prescription, name='view_prescription'),
    path('write_bill/', views.write_bill, name='write_bill'),
    path('bill-generated/', views.bill_generated, name='bill_generated'),
    path('view_bills/', views.view_bills, name='view_bills'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('contact-success/', views.contact_success, name='contact_success'),
    path('wrong-prescription/', views.wrong_prescription, name='wrong_prescription'),
    path('tests/', views.tests, name='tests'),
    path('wrong-patient/', views.wrong_patient, name='wrong_patient'),
]

