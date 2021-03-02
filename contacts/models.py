from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Contacts(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    contact_picture = models.URLField(null=True)
    is_favourite = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.firstname} {self.lastname} : {self.phone_number}'

    class Meta:
        ordering = ["-timestamp"]
