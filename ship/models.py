

#from datetime import date
from django.utils import timezone

from basic.models import Product
from django.db import models

# Create your models here.
#幣別
class Currency(models.Model):
    code = models.CharField(primary_key=True, max_length=3, )
    description = models.CharField(max_length=36, null=False, blank=False)

    def __str__(self):
        return self.code

#客戶
class Customer(models.Model):
    sap_no = models.CharField(primary_key=True, max_length=18) # SAP客尸編號 -9223372036854775808 to 9223372036854775807
    title = models.CharField(max_length=36, null=False, blank=False)
    address = models.CharField(max_length=100, null=True, blank=True)
    contect = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    phone_ext  = models.CharField(max_length=100, null=True, blank=True)
    faxno = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    invalid = models.BooleanField(default=False)#作廢

    create_at = models.DateTimeField(auto_now_add=True, auto_now =False)
    modify = models.DateTimeField(auto_now_add=False, auto_now =True)

    def __str__(self):
        return ("%s : %s" % (self.sap_no,self.title ) )

# 報價單
class QuoteHead(models.Model):
    request_user = models.CharField(max_length=60, null=False, blank=False) #開單人
    ord_date = models.DateField(default=timezone.now) #報價日期
    customer = models.ForeignKey(Customer) #客戶編號
    effective_date = models.DateField( default=timezone.now ) # 報價單有效日期
    currency = models.ForeignKey( Currency )
    invalid = models.BooleanField(default=False) #作廢
    memo = models.TextField(null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True, auto_now =False)
    modify = models.DateTimeField(auto_now_add=False, auto_now =True)


    def get_absoulte_url(self):

        return "/ship/detail/%s/" %( str(self.id) )


# 報價單明細
class QuoteDetail(models.Model):
    quotehead = models.ForeignKey(QuoteHead) #報價單編號
    line_no = models.IntegerField() #行號
    product = models.ForeignKey(Product) # 料號
    unit_price = models.FloatField() # 單價
    line_memo = models.CharField(max_length=50, blank=True, null=True) # 行備註
    invalid = models.BooleanField(default=False) #作廢

    create_at = models.DateTimeField(auto_now_add=True, auto_now =False)
    modify = models.DateTimeField(auto_now_add=False, auto_now =True)

# 訂單
class ShipOrderHead(models.Model):
    request_user = models.CharField(max_length=60, null=False, blank=False)
    ord_date = models.DateField()
    customer_title = models.CharField(max_length=60, null=False, blank=False)
    default_delivery = models.DateField()
    head_memo = models.TextField()

# 訂單明綑
class ShipOrderDetail(models.Model):
    ships_order = models.ForeignKey(ShipOrderHead)
    order_line = models.IntegerField(default=1, blank=False, null=False)
    product = models.ForeignKey(Product)
    unitprice = models.FloatField( default=1, blank=False, null=False)
    ord_amount = models.IntegerField(default=1, blank=False, null=False)
    delivery = models.DateField()
    line_comment = models.CharField(max_length=60, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, auto_now =False)
    modify = models.DateTimeField(auto_now_add=False, auto_now =True)

    class META:
        unique_together = ( "ships_order", "order_line",)
