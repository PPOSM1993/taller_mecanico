from django.db import models

from django.core.validators import RegexValidator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name Category')
    
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name Brand')
    
    def __str__(self):
        return self.name

class Car(models.Model):

    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Brand')
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Category')
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=False, null=True, blank=False)