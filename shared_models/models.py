from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    patient_name = models.CharField(max_length=255,null=True)


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    specialization = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    date_of_birth = models.DateField()
    password = models.CharField(max_length=255) 
    
    def __str__(self):
        return self.name

class Prescriptions(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Bill(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescription = models.ForeignKey(Prescriptions, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)


class Queries(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()