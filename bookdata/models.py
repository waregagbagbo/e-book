from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from autoslug import AutoSlugField
from datetime import datetime
from django.utils.timezone import now


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) 
    kndi_number = models.CharField(max_length=200, unique=True, blank=False)
    speciality = models.CharField(max_length=200, blank=False)
    gender = models.CharField(max_length=20,blank=False)
    #picture = models.ImageField(default='users/default_user.png', upload_to='users', blank=True, null=True)
   # updated = models.DateTimeField(auto_now=False)
    #created = models.DateTimeField(auto_now_add=True, blank=True)
   

    def __str__(self):
        return f'{self.user.username}'  

    #def save(self, *args, **kwargs):        
       # self.slug = slugify(self.user.username)
        #super().save(*args, **kwargs)    

    

# selector choice for gender
Sex =(
   ('M', "Male"),
   ('F', "Female"),
   ('O', "Others"),
)

HealthCenters = (
    ('H',"AAR Hospital"),
    ('H',"Aga Khan University Hospital, Nairobi"),
    ('H',"Avenue Hospital"),
    ('H',"Bristol Park Hospital Tasia Embakas"),
    ('H',"Brother André Medical Center in Dandora"),
    ('H',"Coptic Hospital Nursing Hospital"),
    ('H',"Gertrude's Children's Hospital"),
    ('H',"Karen Hospital"),
    ('H',"Kenyatta Hospital"),
    ('H',"Mama Lucy Kibaki"),
    ('H',"Mater Hospital"),
)

class LogBookData(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=20, null=True)
    patient_gender = models.CharField(max_length=20, blank=False, choices=Sex, help_text="select above", default=True)
    patient_age = models.CharField(max_length=20, blank=False)
    date_created = models.DateField("entry date (%yy-%mm-%dd)", auto_now_add=False)
    supervisor_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    supervisor_contact = PhoneNumberField(validators=[supervisor_regex], max_length=17, blank=False, null=True) # validators should be a list
    hospital = models.CharField(max_length=200, blank=False, choices=HealthCenters)
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
    

    
    

    

