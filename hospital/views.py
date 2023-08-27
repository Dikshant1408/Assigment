# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from shared_models.models import Patient, Appointment, Doctor, Prescriptions, Bill, Queries

def index(request):
    template = loader.get_template('hms_landing_page.html')
    return HttpResponse(template.render())

def patient(request):
    template = loader.get_template('patient.html')
    return HttpResponse(template.render())

def patient_landing(request):
    return render(request, 'patient_landing.html')

def registration_success(request):
    return render(request, 'registration_success.html')

def appointment_success(request):
    return render(request, 'appointment_success.html')

def prescription_saved(request):
    return render(request, 'prescription_saved.html')

def bill_generated(request):
    return render(request, 'bill_generated.html')

def contact_success(request):
    return render(request, 'contact_success.html')

def wrong_prescription(request):
    return render(request, 'wrong_prescription.html')

def tests(request):
    return render(request, 'tests.html')

def wrong_patient(request):
    return render(request, 'wrong_patient.html')

def patient_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        contact_number = request.POST['contact_number']
        gender = request.POST['gender']
        age = request.POST['age']
        patient = Patient(name=name, email=email, password=password, contact_number=contact_number, gender=gender, age=age)
        patient.save()
    
    # Redirect to the signup success page
        return redirect('registration_success')
    else:
        return render(request, 'patient_landing.html')
    

def registration_success(request):
    if request.method == 'POST':
        # check if the "Login here" button was pressed
        if request.POST.get('login_button'):
            # redirect to the login page
            return redirect('patient_landing')
    # render the signup success page template
    return render(request, 'registration_success.html')


def login_view(request):
    if request.method == 'POST':
        patient_email = request.POST.get('email')
        patient_password = request.POST.get('password')
        user = Patient.objects.filter(email=patient_email).first()
        if user is not None and user.password == patient_password:
            request.session['patient'] = patient_email
            return redirect('patient_dashboard')
        else:
            error_message = 'Invalid login credentials. Please try again.'
            return render(request, 'wrong_login_credentials.html', {'error_message': error_message})
    else:
        return render(request, 'patient_landing.html')


def patient_dashboard(request):
    patient_email = request.session.get('patient')
    if patient_email is None:
        return redirect('patient_login')
    patient = Patient.objects.get(email=patient_email)
    appointments = Appointment.objects.filter(patient=patient)
    return render(request, 'patient_dashboard.html', {'patient': patient, 'appointments': appointments})


def fix_appointment(request):
    patient_email = request.session.get('patient')
    if patient_email is None:
        return redirect('patient_login')
    patient = Patient.objects.get(email=patient_email)
    doctors = Doctor.objects.all()
    if request.method == 'POST':
        doctor_name = request.POST.get('doctor')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        doctor = Doctor.objects.get(name=doctor_name)  # retrieve Doctor object based on name
        appointment = Appointment(patient=patient, patient_name=patient.name, doctor_name=doctor.name, appointment_date=appointment_date, appointment_time=appointment_time)
        appointment.save()
        return redirect('appointment_success')
    return render(request, 'fix_appointment.html', {'doctors': doctors})


def doctor_login(request):
    if request.method == 'POST':
        doctor_email = request.POST.get('email')
        doctor_password = request.POST.get('password')
        user = Doctor.objects.filter(email=doctor_email).first()
        if user is not None and user.password == doctor_password:
            request.session['doctor'] = doctor_email
            return redirect('doctor_dashboard')
        else:
            error_message = 'Invalid login credentials. Please try again.'
            return render(request, 'wrong_login_credentials_doctor.html', {'error_message': error_message})
    else:
        return render(request, 'doctor_login.html')
    

def doctor_dashboard(request):
    doctor_email = request.session.get('doctor')
    if doctor_email is None:
        return redirect('doctor_login')
    doctor = Doctor.objects.get(email=doctor_email)
    return render(request, 'doctor_dashboard.html', {'doctor': doctor})


def view_appointments(request):
    doctor_email = request.session.get('doctor')
    if doctor_email is None:
        return redirect('doctor_login')
    doctor = Doctor.objects.get(email=doctor_email)
    doctor_appointments = Appointment.objects.filter(doctor_name=doctor.name)
    context = {'appointments': doctor_appointments}
    return render(request, 'view_appointments.html', context)


def delete_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.delete()
    return redirect('view_appointments')

def write_prescription(request):
    doctor_email = request.session.get('doctor')
    if doctor_email is None:
        return redirect('doctor_login')
    doctor = Doctor.objects.get(email=doctor_email)
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        content = request.POST.get('content')
        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            return redirect('wrong_patient')
        prescription = Prescriptions(doctor=doctor, patient=patient, content=content)
        prescription.save()
        return redirect('prescription_saved')
    context = {'doctor': doctor}
    return render(request, 'write_prescription.html', context)

def view_prescription(request):
    patient_email = request.session.get('patient')
    if patient_email is None:
        return redirect('patient_login')
    patient = Patient.objects.get(email=patient_email)
    patient_prescriptions = Prescriptions.objects.filter(patient_id=patient.id)
    context = {'prescriptions': patient_prescriptions}
    return render(request, 'view_prescription.html', context)

def write_bill(request):
    doctor_email = request.session.get('doctor')
    if doctor_email is None:
        return redirect('doctor_login')
    doctor = Doctor.objects.get(email=doctor_email)
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        prescription_id = request.POST.get('prescription_id')
        prescription = Prescriptions.objects.filter(id=prescription_id, patient__id=patient_id, doctor=doctor).first()
        if prescription is None:
            return redirect('wrong_prescription')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        bill = Bill(doctor=doctor, patient=prescription.patient, prescription=prescription, description=description, amount=amount)
        bill.save()
        return redirect('bill_generated')
    context = {'doctor': doctor}
    return render(request, 'write_bills.html', context)

def view_bills(request):
    patient_email = request.session.get('patient')
    if patient_email is None:
        return redirect('patient_login')
    patient = Patient.objects.get(email=patient_email)
    patient_bills = Bill.objects.filter(patient_id=patient.id)
    context = {'bills': patient_bills}
    return render(request, 'view_bill.html', context)

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Queries(name=name, email=email, message=message)
        contact.save()
        return redirect('contact_success') # redirect to a success page
    return render(request, 'hms_landing_page.html')