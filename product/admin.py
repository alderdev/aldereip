from django.contrib import admin
from .models import (Product, ProductCategory, CycleStatus, )
# Register your models here.

admin.site.register(CycleStatus)
admin.site.register(ProductCategory)
admin.site.register(Product)
