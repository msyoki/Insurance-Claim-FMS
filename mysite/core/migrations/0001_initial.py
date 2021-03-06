# Generated by Django 2.1.5 on 2021-02-19 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import functools
import mysite.core.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClaimCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='LifeClaim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_number', models.CharField(max_length=200)),
                ('national_id', models.FileField(upload_to=functools.partial(mysite.core.models._update_filename, *(), **{'path': 'RootFile/Life_Claims/National_ID'}))),
                ('bill_invoice', models.FileField(upload_to=functools.partial(mysite.core.models._update_filename, *(), **{'path': 'RootFile/Life_Claims/Bill_Invoice'}))),
                ('claim_form', models.FileField(upload_to=functools.partial(mysite.core.models._update_filename, *(), **{'path': 'RootFile/Life_Claims/Claim_Form'}))),
                ('medical_report', models.FileField(upload_to=functools.partial(mysite.core.models._update_filename, *(), **{'path': 'RootFile/Life_Claims/Medical_Report'}))),
                ('payslip', models.FileField(upload_to=functools.partial(mysite.core.models._update_filename, *(), **{'path': 'RootFile/Life_Claims/Payslip'}))),
                ('sick_off_sheet', models.FileField(upload_to=functools.partial(mysite.core.models._update_filename, *(), **{'path': 'RootFile/Life_Claims/Sick_Off_Sheet'}))),
                ('pin_certificate', models.FileField(upload_to=functools.partial(mysite.core.models._update_filename, *(), **{'path': 'RootFile/Life_Claims/Pin_Certificate'}))),
                ('death_certificate', models.FileField(upload_to=functools.partial(mysite.core.models._update_filename, *(), **{'path': 'RootFile/Life_Claims/Death_Certificate'}))),
                ('burial_permit', models.FileField(upload_to=functools.partial(mysite.core.models._update_filename, *(), **{'path': 'RootFile/Life_Claims/Burial_Permit'}))),
            ],
        ),
        migrations.CreateModel(
            name='MotorClaim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_registration', models.CharField(max_length=200)),
                ('image_one', models.ImageField(upload_to='images/')),
                ('image_two', models.ImageField(upload_to='images/')),
                ('image_three', models.ImageField(upload_to='images/')),
                ('claim_form', models.FileField(upload_to=functools.partial(mysite.core.models._update_filename, *(), **{'path': 'RootFile/Motor_Claims/Claim_Form/'}))),
                ('police_abstract', models.FileField(upload_to=functools.partial(mysite.core.models._update_filename, *(), **{'path': 'RootFile/Motor_Claims/Police_Abstract/'}))),
                ('drivers_license', models.FileField(upload_to=functools.partial(mysite.core.models._update_filename, *(), **{'path': 'RootFile/Motor_Claims/Drivers_License/'}))),
                ('statement_of_loss', models.FileField(upload_to=functools.partial(mysite.core.models._update_filename, *(), **{'path': 'RootFile/Motor_Claims/Statement_Of_Loss/'}))),
                ('incident_report', models.FileField(upload_to=functools.partial(mysite.core.models._update_filename, *(), **{'path': 'RootFile/Motor_Claims/Incident_Report/'}))),
                ('national_id', models.FileField(upload_to=functools.partial(mysite.core.models._update_filename, *(), **{'path': 'RootFile/Motor_Claims/National_ID/'}))),
                ('towing_receipt', models.FileField(upload_to=functools.partial(mysite.core.models._update_filename, *(), **{'path': 'RootFile/Motor_Claims/Towing_Receipt/'}))),
                ('log_book', models.FileField(upload_to=functools.partial(mysite.core.models._update_filename, *(), **{'path': 'RootFile/Motor_Claims/Log_Book'}))),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
