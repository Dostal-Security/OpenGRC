from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BusinessUnit(models.Model):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ThirdParty(models.Model):
    class Meta:
        verbose_name_plural = "third parties"

    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=100)
    organizations = models.ManyToManyField(Organization)

    def __str__(self):
        return self.name
