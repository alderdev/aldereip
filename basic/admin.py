from django.contrib import admin


from .models import CycleStatus, Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'sap_no', 'product_desc', 'specification' ,'cycle_status',)



admin.site.register(CycleStatus)
admin.site.register(Product, ProductAdmin)
