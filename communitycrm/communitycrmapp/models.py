from django.db import models
from django.utils import timezone

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=12)
    email = models.EmailField()
    fbpagelink = models.URLField()
    address = models.TextField()
    meetuplink = models.URLField()
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
