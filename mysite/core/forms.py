from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Claim,Category,MotorClaim,LifeClaim


# Choices=Category.objects.all().values_list("name","name")
# choice_list=[]

# for item in Choices:
#     choice_list.append(item)

class MotorClaimForm(forms.ModelForm):
    class Meta:
        model=MotorClaim
        fields=[
            "vehicle_registration",
            "image_one",
            "image_three",
            "claim_form",
            "police_abstract",
            "drivers_license",
            "statement_of_loss",
            "incident_report",
            "national_id",
            "towing_receipt",
            "log_book",
        ]


class LifeClaimForm(forms.ModelForm):
    class Meta:
        model=LifeClaim
        fields=[
            "policy_number",
            "national_id",
            "bill_invoice",
            "claim_form",
            "medical_report",
            "payslip",
            "sick_off_sheet",
            "pin_certificate",
            "death_certificate",
            "burial_permit",
        ]






class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = [ 'category' ]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email','password1','password2']

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')

