from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
# class dashboard(models.Model):
#     user = models.ForeignKey(User , on_delete = models.SET_NULL, null = True, blank = True)
#     # phone = models.CharField(max_length=10, blank=True, null=True)


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    # full_name = models.CharField(max_length=50, blank= True, null=True)
    def __str__(self):
        return self.first_name

class Specialization(models.Model):
    specialization_name = models.CharField(max_length=250)

    def __str__(self):
        return self.specialization_name

class DoctorInfo(models.Model):
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nmcNo = models.IntegerField()
    experience = models.IntegerField()
    specialization = models.ForeignKey(Specialization, on_delete = models.SET_NULL, blank = True, null = True)
    image =  models.ImageField(upload_to='doctor/')
    def __str__(self):
        return self.name


