from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField


class HackatonChallenge(models.Model):
    title = models.CharField(max_length=255)
    # TODO turn the slug field to false in production
    slug = models.SlugField(null=True, unique=True)
    text = RichTextField(blank=True, null=True, config_name='awesome_ckeditor')
    challenge_avatar = models.ImageField(upload_to='challenge_avatar', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("hackatonchallenge_details", kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
