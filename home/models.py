from django.db import models
from django.contrib.auth.models import User


class SosUser(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=50)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class SosMessage(models.Model):
    maps_location = models.CharField(max_length=300, null=True)
    number_of_people = models.IntegerField()
    extra_message = models.TextField(max_length=1000)
    medical_assistance = models.BooleanField()
    sosuser = models.ForeignKey(SosUser, on_delete=models.CASCADE)


class MilitarySos(models.Model):
    sos_message = models.OneToOneField(SosMessage, on_delete=models.CASCADE)


class MedicalSos(models.Model):
    sos_message = models.OneToOneField(SosMessage, on_delete=models.CASCADE)
