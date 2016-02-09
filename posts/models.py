from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    image = models.FileField(null=True, blank=True)
    content = models.TextField()
    updated = models.DateTimeField('Was updated', auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField('Was created', auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'id': self.id})

    class Meta:
        ordering = ["-updated", "-timestamp"]
