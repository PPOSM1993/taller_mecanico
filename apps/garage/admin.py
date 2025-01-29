from django.contrib import admin
from .models import *

# Register your models here.

#class CategoryInline(admin.TabularInline):
#    model = Category

#class CategoryAdmin(admin.ModelAdmin):
#    inlines = [
#        CategoryInline
#    ]

admin.site.register(Category)

