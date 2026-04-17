from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField


class userinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = PhoneNumberField()
    address = models.CharField(max_length=25, default='none')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'User Advance Information'
        verbose_name_plural = 'Profile Details'