from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Core(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)
    snip = models.TextField(null=True)
    series = models.CharField(max_length=255)
    publishing = models.CharField(max_length=255)
    sketcher = models.ForeignKey(User, on_delete=models.Cascade, related_name='coreapp')
    updated = models.DateTimeField(auto_now=True)
    published_date = modles.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('coreapp:inedex', args=[self.slug])

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title


