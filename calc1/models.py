from django.db import models

# Create your models here.
class Course(models.Model):
    credits = models.DecimalField(max_digits=3, decimal_places=1)
    grade = models.CharField(max_length=1)