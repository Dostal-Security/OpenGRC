from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=50)

    def __str__(self):
        return self.name
