from django.contrib import admin
from .models import LifeClaim,Category,MotorClaim,Profile,Claim
# Register your models here.
admin.site.register(LifeClaim)
admin.site.register(Category)
admin.site.register(MotorClaim)
admin.site.register(Profile)
admin.site.register(Claim)
