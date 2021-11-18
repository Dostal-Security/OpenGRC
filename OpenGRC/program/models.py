from django.db import models
from framework.models import Framework
from organization.models import Organization, BusinessUnit, Contact

# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    business_unit = models.ForeignKey(
        BusinessUnit, on_delete=models.CASCADE, null=True, blank=True
    )
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    frameworks = models.ManyToManyField(Framework)

    def __str__(self):
        return self.name
