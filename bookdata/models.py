from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) 
    kndi_number = models.CharField(max_length=200, blank=False)
    speciality = models.CharField(max_length=200, blank=False)
    gender = models.CharField(max_length=20,blank=False)    

    def __str__(self):
        return self.speciality
    

# selector choice for gender
Sex =(
   ('Male','Male'),
   ('Female','Female'),
   ('Others','Others'),
)

HealthCenters = (
    ('AAR',"AAR Hospital"),
    ('Aga Khan',"Aga Khan University Hospital, Nairobi"),
    ('Avenue',"Avenue Hospital"),
    ('Bristol Park Hospital Tasia Embakasi',"Bristol Park Hospital Tasia Embakasi"),
    ('Brother André Medical Center in Dandora',"Brother André Medical Center in Dandora"),
    ('Coptic Hospital Nursing Hospital',"Coptic Hospital Nursing Hospital"),
    ('',"Gertrude's Children's Hospital"),
    ('',"Karen Hospital"),
    ('',"Kenyatta Hospital"),
    ('',"Mama Lucy Kibaki"),
    ('',"Mater Hospital"),
)

class LogBookData(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=20, null=True)
    patient_gender = models.CharField(max_length=20, blank=False, choices=Sex, help_text="select above", default=True)
    patient_age = models.CharField(max_length=20, blank=False)
    date_created = models.DateField("entry date (%yy-%mm-%dd)", auto_now_add=False)
    supervisor_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    supervisor_contact = PhoneNumberField(validators=[supervisor_regex], max_length=17, blank=False, null=True) # validators should be a list
    hospital = models.CharField(max_length=200, blank=False, choices=HealthCenters, default=True)
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
    
   #def get_absolute_url(self):
        #return reverse("main")
    

    
    

    

