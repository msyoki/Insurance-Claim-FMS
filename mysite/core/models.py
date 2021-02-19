from django.db import models
from django.contrib.auth.models import User


import os
from functools import partial







class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
 
    def __str__(self):
        return f'{self.user.username} Profile'




 
class Category(models.Model):
    name=models.CharField(max_length=200)


    class Meta:
        verbose_name_plural="Category"

    def __str__(self):
        return self.name



class Claim(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    applicant = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural="Claim"

    def __str__(self):
        return self.category.name


# reusable functions that rename uploaded files in motor and life claim filefields

def _update_filename(instance, filename, path):
    path = path

    filename = instance.applicant.username

    return os.path.join(path, filename)

def upload_to(path):
    return partial(_update_filename, path=path)




class MotorClaim(models.Model):
    vehicle_registration = models.CharField(max_length=200)
    image_one = models.ImageField(upload_to='RootFile/Motor_Claims/images/')
    image_two = models.ImageField(upload_to='RootFile/Motor_Claims/images/')
    image_three = models.ImageField(upload_to='RootFile/Motor_Claims/images/')
    claim_form = models.FileField(upload_to=upload_to('RootFile/Motor_Claims/Claim_Form/'))
    police_abstract = models.FileField(upload_to=upload_to('RootFile/Motor_Claims/Police_Abstract/'))
    drivers_license= models.FileField(upload_to=upload_to('RootFile/Motor_Claims/Drivers_License/'))
    statement_of_loss= models.FileField(upload_to=upload_to('RootFile/Motor_Claims/Statement_Of_Loss/'))
    incident_report= models.FileField(upload_to=upload_to('RootFile/Motor_Claims/Incident_Report/'))
    national_id= models.FileField(upload_to=upload_to('RootFile/Motor_Claims/National_ID/'))
    towing_receipt= models.FileField(upload_to=upload_to('RootFile/Motor_Claims/Towing_Receipt/'))
    log_book= models.FileField(upload_to=upload_to('RootFile/Motor_Claims/Log_Book'))

    def __str__(self):
        return self.vehicle_registration 



class LifeClaim(models.Model):
    policy_number = models.CharField(max_length=200)
    national_id = models.FileField(upload_to=upload_to('RootFile/Life_Claims/National_ID'))
    bill_invoice = models.FileField(upload_to=upload_to('RootFile/Life_Claims/Bill_Invoice'))
    claim_form = models.FileField(upload_to=upload_to('RootFile/Life_Claims/Claim_Form'))
    medical_report = models.FileField(upload_to=upload_to('RootFile/Life_Claims/Medical_Report'))
    payslip = models.FileField(upload_to=upload_to('RootFile/Life_Claims/Payslip'))
    sick_off_sheet = models.FileField(upload_to=upload_to('RootFile/Life_Claims/Sick_Off_Sheet'))
    pin_certificate = models.FileField(upload_to=upload_to('RootFile/Life_Claims/Pin_Certificate'))
    death_certificate = models.FileField(upload_to=upload_to('RootFile/Life_Claims/Death_Certificate'))
    burial_permit = models.FileField(upload_to=upload_to('RootFile/Life_Claims/Burial_Permit'))

    def __str__(self):
        return self.policy_number



