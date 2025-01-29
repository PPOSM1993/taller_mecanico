from django.db import models

from django.core.validators import RegexValidator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name Category')
    
    def __str__(self):
        return self.name


