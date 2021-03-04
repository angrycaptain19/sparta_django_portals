from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_participant = models.BooleanField(default=False)
    is_local_gov_unit = models.BooleanField(default=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, )

    phone = models.CharField(max_length=50)
    gender_choices = {
        ('male', 'male'),
        ('female', 'female'),
    }
    gender = models.CharField(max_length=50, choices=gender_choices, null=True)
    birth_date = models.DateField(blank=True, null=True)
    # Address info
    # TODO Add list of ph province 2/22/2021
    city_province = models.CharField(max_length=100)
    address = models.TextField()
    # other info
    occupation = models.CharField(max_length=100)
    participant_avatar = models.ImageField(upload_to='participant_avatar', blank=True)


class LocalGovUnit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # TODO turn the slug field to false in production
    slug = models.SlugField(null=True, unique=True)
    phone = models.CharField(max_length=50)
    # Address info
    region = models.CharField(max_length=100)
    city_province = models.CharField(max_length=100)
    address = models.TextField()
    lgu_avatar = models.ImageField(upload_to='lgu_avatar', blank=True)
    lgu_detail_avatar = models.ImageField(upload_to='lgu_detail_avatar', blank=True)

    def get_absolute_url(self):
        return reverse("localgovernmentunit_details", kwargs={'slug': self.slug})
