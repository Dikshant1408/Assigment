from django.shortcuts import render
from . models import Patient
# Create your views here.

def informer(request):
    email = request.GET.get("loggedPatient")
    password = request.GET.get("password")
    data = Patient.objects.filter(email=email)
    for info in data:
        print(info)
        if info.email == email and info.password == password:

            patient_info = {
                "access" : "Granted"
            }

        else:
            patient_info = {
                "access" : "Denied"
            }


