from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phoneNumber = models.CharField(max_length=13)
    
    def __str__(self):
        return self.name
