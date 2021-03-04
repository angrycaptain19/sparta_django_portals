from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField


class HomeCarouselPhoto(models.Model):
    carousel_photo = models.ImageField(upload_to='carousel_photo', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
