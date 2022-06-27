from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    kndi_number = models.CharField(max_length=200, unique=True, blank=False)
    speciality = models.CharField(max_length=200, blank=False)
    gender = models.CharField(max_length=20,blank=False)
    def __str__(self):
        return self.user.username   
    

# selector choice for gender
Sex =(
   ('M', "Male"),
   ('F', "Female"),
   ('O', "Others"),
)

class LogBookData(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=20, null=True)
    patient_gender = models.CharField(max_length=20, blank=False, choices=Sex, help_text="select above", default=True)
    patient_age = models.CharField(max_length=20, blank=False)
    date_created = models.DateField("entry date (2022/mm/dd)", auto_now_add=False)
    supervisor_contact = models.CharField(max_length=20, blank=False, null=True)
    hospital = models.CharField(max_length=200, blank=False)
    #imaging_results = models.ImageField()
    biochemistry_results = models.BooleanField(null=True)
    nutrition_diagnosis = models.CharField(max_length=1000, blank=True)
    services_rendered = models.CharField(max_length=300, blank=True)
    clinical_diagnosis = models.BooleanField(null=True)
    follow_up_plan = models.CharField(max_length=200)
    outcome = models.CharField(max_length=2000)
    #notes = models.TextField()

    def __str__(self):
        return self.patient_name    
    
    class Meta:
        ordering = ('-date_created',)

    
    

    

