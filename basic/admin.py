from django.contrib import admin


from .models import CycleStatus, Product, ProductCategory
#from . import models
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'sap_no', 'product_desc', 'specification', 'category' ,'cycle_status' )


admin.site.register(ProductCategory)
admin.site.register(CycleStatus)
admin.site.register(Product, ProductAdmin)
