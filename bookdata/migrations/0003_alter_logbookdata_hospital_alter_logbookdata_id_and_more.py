# Generated by Django 4.1 on 2022-09-16 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookdata', '0002_auto_20220809_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logbookdata',
            name='hospital',
            field=models.CharField(choices=[('AAR', 'AAR Hospital'), ('Aga Khan', 'Aga Khan University Hospital, Nairobi'), ('Avenue', 'Avenue Hospital'), ('Bristol Park Hospital Tasia Embakasi', 'Bristol Park Hospital Tasia Embakasi'), ('Brother André Medical Center in Dandora', 'Brother André Medical Center in Dandora'), ('Coptic Hospital Nursing Hospital', 'Coptic Hospital Nursing Hospital'), ('', "Gertrude's Children's Hospital"), ('', 'Karen Hospital'), ('', 'Kenyatta Hospital'), ('', 'Mama Lucy Kibaki'), ('', 'Mater Hospital')], default=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='logbookdata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='logbookdata',
            name='patient_gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default=True, help_text='select above', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
