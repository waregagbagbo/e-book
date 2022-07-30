from django.contrib import admin
from .models import *

# Register your models here.
class LogBookAdmin(admin.ModelAdmin):
    model = LogBookData
    list_display = ('patient_name','patient_gender','patient_age','supervisor_contact','hospital','biochemistry_results',
    'clinical_diagnosis',)
    list_filter = ('date_created',)

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('kndi_number','speciality','gender',)
    list_display_links = ('speciality',)


admin.site.register(Profile,ProfileAdmin)
admin.site.register(LogBookData,LogBookAdmin)

# change default django admin interface
admin.site.site_header = 'Nutritions Academy'