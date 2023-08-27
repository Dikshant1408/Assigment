# views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Signupdetails
from django.template import loader
from django.contrib.auth.models import User
from shared_models.models import Patient, Doctor, Queries

def index(request):
    template = loader.get_template('adminlanding.html')
    return HttpResponse(template.render())

def signup_success(request):
    template = loader.get_template('signup_success.html')
    return HttpResponse(template.render())

def admin_dashboard(request):
    template = loader.get_template('admin_dashboard.html')
    return HttpResponse(template.render())

def wrong_login_credentials(request):
    template = loader.get_template('wrong_login_credentials.html')
    return HttpResponse(template.render())


def manage_doctors(request):
    return render(request, 'manage_doctors.html')


def register_doctor(request):
    return render(request, 'register_doctor.html')


def registration_successful(request):
    template = loader.get_template('registration_successful.html')
    return HttpResponse(template.render())



def adminlanding(request):
    if request.method == 'POST':
        Name = request.POST['fullname']
        Email = request.POST['email']
        Username = request.POST['Username']
        password = request.POST['Password']
        
        # Hash the password using SHA-256 algorithm
        #hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        admin = Signupdetails(admin_name=Name, admin_email=Email, admin_username=Username, admin_password=password)
        admin.save()

        # Redirect to the signup success page
        return redirect('signup_success')
    else:
        return render(request, 'adminlanding.html')


def signup_success(request):
    if request.method == 'POST':
        # check if the "Login here" button was pressed
        if request.POST.get('login_button'):
            # redirect to the login page
            return redirect('login')
    # render the signup success page template
    return render(request, 'signup_success.html')


#def hash_password(password):
#    salt = b'some_salt'  # use a different salt for each user
#    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000).hex()


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('admin_username')
        password = request.POST.get('admin_password')
        user = Signupdetails.objects.filter(admin_username=username).first()
        if user is not None and user.admin_password == password:
            request.session['admin'] = True
            return redirect('admin_dashboard')
        else:
            error_message = 'Invalid login credentials. Please try again.'
            return render(request, 'wrong_login_credentials.html', {'error_message': error_message})
    else:
        return render(request, 'adminlanding.html')


def admin_dashboard(request):
    if not request.session.get('admin'):
        return redirect('admin_login')
    return render(request, 'admin_dashboard.html')


def adminlanding(request):
    if request.method == 'POST':
        Name = request.POST['fullname']
        Email = request.POST['email']
        Username = request.POST['Username']
        password = request.POST['Password']
        
        # Hash the password using SHA-256 algorithm
        #hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        admin = Signupdetails(admin_name=Name, admin_email=Email, admin_username=Username, admin_password=password)
        admin.save()

        # Redirect to the signup success page
        return redirect('signup_success')
    else:
        return render(request, 'adminlanding.html')


def doctor_registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        specialization = request.POST['specialization']
        gender = request.POST['gender']
        date_of_birth = request.POST['date_of_birth']
        password = request.POST['password']
        
        doctor = Doctor(name=name, email=email, phone=phone, specialization=specialization,
                        gender=gender, date_of_birth=date_of_birth, password=password)
        doctor.save()

        # Redirect to the registration success page
        return redirect('registration_successful')
    else:
        return render(request, 'register_doctor.html')


def registration_successful(request):
    if request.method == 'POST':
        # check if the "Back to dashboard" button was pressed
        if request.POST.get('dashboard_button'):
            # redirect to the dashboard page
            return redirect('admin_dashboard')
    # render the registration success page template
    return render(request, 'registration_successful.html')


def doctor_list_display(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'doctor_list.html', context)


def doctor_list(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            try:
                doctor = Doctor.objects.get(email=email)
                print(doctor)
                doctor.delete()
            except Doctor.DoesNotExist:
                pass
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})


def patient_list(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            try:
                patient = Patient.objects.get(email=email)
                print(patient)
                patient.delete()
            except Patient.DoesNotExist:
                pass
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def view_queries(request):
    admin_username = request.session.get('admin')
    if admin_username is None:
        return redirect('adminlanding')
    if request.method == 'POST':
        query_id = request.POST.get('id')
        if query_id:
            try:
                query = Queries.objects.get(id=query_id)
                query.delete()
            except Queries.DoesNotExist:
                pass
    queries = Queries.objects.all()
    context = {'queries': queries}
    return render(request, 'view_queries.html', context)
