from django.contrib import admin

from .models import Customer, QuoteHead, QuoteDetail, ShipOrderHead, ShipOrderDetail,Currency
# Register your models here.


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ( 'code', 'description',)

class QuoteDetailInline(admin.TabularInline):
    model = QuoteDetail

class QuoteAdmin(admin.ModelAdmin):
    inlines = [QuoteDetailInline,]


class ShipOrderDetailInline(admin.TabularInline):
    model = ShipOrderDetail

class ShipOrderAdmin(admin.ModelAdmin):
    inlines = [ShipOrderDetailInline,]



class CustomerAdmin(admin.ModelAdmin):
    list_display = ( 'sap_no', 'title','contect','phone','phone_ext', 'email', 'address' ,)



admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(QuoteHead, QuoteAdmin)
admin.site.register(ShipOrderHead, ShipOrderAdmin)
