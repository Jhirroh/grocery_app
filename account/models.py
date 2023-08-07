from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    avatar = models.ImageField(upload_to='img/avatar/', null=True, default='img/avatar/default.png')
    dob = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    mobile = models.PositiveBigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username
