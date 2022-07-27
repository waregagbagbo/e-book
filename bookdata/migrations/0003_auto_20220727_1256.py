# Generated by Django 3.1.7 on 2022-07-27 12:56

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('bookdata', '0002_auto_20220628_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logbookdata',
            name='date_created',
            field=models.DateField(verbose_name='entry date (%yy-%mm-%dd)'),
        ),
        migrations.AlterField(
            model_name='logbookdata',
            name='supervisor_contact',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=17, null=True, region=None, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
