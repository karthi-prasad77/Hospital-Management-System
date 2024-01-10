from django.db import models
from multiselectfield import MultiSelectField
import datetime

# Create your models here.

SYMPTOMS = (
        ('Fever', 'Fever'),
        ('Dry cough', 'Dry cough'),
        ('Tiredness', 'Tiredness'),
        ('Aches and pains', 'Aches and pains'),
        ('Sore throat', 'Sore throat'),
        ('Diarrhoea', 'Diarrhoea'),
)

class Departments(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Bed(models.Model):
    bed_Number = models.CharField(max_length=50)
    ward = models.CharField(max_length=50, default="Ward-0")
    occupied = models.BooleanField()
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.bed_Number} - {self.ward} - {self.department}"
  

class Patient(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    patient_relative_name = models.CharField(max_length=50, null=True)
    patient_relative_contact = models.CharField(max_length=15, null=True)
    address = models.TextField()
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)
    symptoms = MultiSelectField(choices=SYMPTOMS, max_choices=2, null=True)
    prior_ailnments = models.TextField()
    bed = models.OneToOneField(Bed, on_delete=models.SET_NULL, null=True, blank=True)
    dob = models.DateField(null=True)
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE, null=True)
    doctors_notes = models.TextField(null=True, blank=True)
    doctors_visiting_time = models.CharField(null=True, max_length=50, blank=True)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    
  
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name