# Generated by Django 4.1 on 2022-09-16 08:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kndi_number', models.CharField(max_length=200, null=True)),
                ('speciality', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=20)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LogBookData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=20, null=True)),
                ('patient_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default=True, help_text='select above', max_length=20)),
                ('patient_age', models.CharField(max_length=20)),
                ('date_created', models.DateField(verbose_name='entry date (%yy-%mm-%dd)')),
                ('supervisor_contact', phonenumber_field.modelfields.PhoneNumberField(max_length=17, null=True, region=None, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('hospital', models.CharField(choices=[('AAR', 'AAR Hospital'), ('Aga Khan', 'Aga Khan University Hospital, Nairobi'), ('Avenue', 'Avenue Hospital'), ('Bristol Park Hospital Tasia Embakasi', 'Bristol Park Hospital Tasia Embakasi'), ('Brother André Medical Center in Dandora', 'Brother André Medical Center in Dandora'), ('Coptic Hospital Nursing Hospital', 'Coptic Hospital Nursing Hospital'), ('', "Gertrude's Children's Hospital"), ('', 'Karen Hospital'), ('', 'Kenyatta Hospital'), ('', 'Mama Lucy Kibaki'), ('', 'Mater Hospital')], default=True, max_length=200)),
                ('biochemistry_results', models.BooleanField(null=True)),
                ('nutrition_diagnosis', models.CharField(blank=True, max_length=1000)),
                ('services_rendered', models.CharField(blank=True, max_length=300)),
                ('clinical_diagnosis', models.BooleanField(null=True)),
                ('follow_up_plan', models.CharField(max_length=200)),
                ('outcome', models.CharField(max_length=2000)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
