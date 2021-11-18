from django.db import models

# Create your models here.
class Framework(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Control(models.Model):
    framework = models.ForeignKey(Framework, on_delete=models.CASCADE)
    control_group_id = models.CharField(max_length=50, verbose_name="Control Group ID")
    control_group_title = models.TextField()
    control_group_description = models.TextField(blank=True, null=True)
    control_item_id = models.CharField(max_length=15, verbose_name="Control Item ID")
    control_item_title = models.TextField()
    control_item_description = models.TextField()
    recommended_evidence = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.control_item_title
