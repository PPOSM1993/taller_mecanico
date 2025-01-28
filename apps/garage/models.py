from django.db import models

from django.core.validators import RegexValidator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name Category', unique=True, null=False, blank=False)
    
    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Category, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']

class Brand(models.Model):
    name = models.CharField(max_length=150, verbose_name='Brand', unique=True, null=False, blank=False)
    
    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Category, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['id']

class Custom(models.Model):
    pass


class Car(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Category')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Brand')
    model = models.CharField(max_length=150, verbose_name='Car Model', unique=False, null=True, blank=False)
    year = models.IntegerField(default=0, verbose_name='Year Car')
    patent_regex = RegexValidator(
        regex=r'/^[A-Z]{3}\d{3}$/', message="Formato Patente Incorrecto.")
    patent = models.CharField(
        validators=[patent_regex], max_length=12, unique=True, verbose_name='Patent')

    def __str__(self):
        return self.model
    
    def __str__(self):
        return self.get_full_name()
    
    def get_full_name(self):
        return '{} / {}'.format(self.model, self.patent)

    def toJSON(self):
        item = model_to_dict(self)
        item['full_name'] = self.get_full_name()
        return item
    
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
        ordering = ['id']
