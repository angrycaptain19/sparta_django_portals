from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField


class LocalGovernmentChallenge(models.Model):
    localgovernmentunit = models.ForeignKey('accounts.User',
                                            on_delete=models.CASCADE,
                                            related_name='localgovernmentchallenges'
                                            )
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)
    text = RichTextField(blank=True, null=True, config_name='awesome_ckeditor')
    challenge_avatar = models.ImageField(upload_to='lgu_challenge_avatar', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("localgovernmentChallenge_details", kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

