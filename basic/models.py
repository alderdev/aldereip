from django.db import models

# Create your models here.


#料品生命週期狀態
class CycleStatus(models.Model):
    description = models.CharField(max_length=36, null=False, blank=False)
    invalid = models.BooleanField(default=False)

    def __str__(self):
        return self.description

#料品
class Product(models.Model):
    sap_no = models.BigIntegerField(primary_key=True) # SAP料號 -9223372036854775808 to 9223372036854775807
    product_desc = models.CharField(max_length=36, null=False, blank=False) # 品名
    specification = models.CharField(max_length=100, null=False, blank=False) # 規格
    cycle_status = models.ForeignKey(CycleStatus) # 料品狀態
    create_at = models.DateTimeField(auto_now_add=True, auto_now =False) #
    modify = models.DateTimeField(auto_now_add=False, auto_now =True) #

    def __str__(self):
        return ("%s : %s" % (self.sap_no,self.product_desc ) )

#單據類型
class OrderCategory(models.Model):
    description = models.CharField(max_length=36, null=False, blank=False)
    order_squence = models.IntegerField(default=1000, null=False, blank=False)
    invalid = models.BooleanField(default=False)

    def __str__(self):
        return self.description

#ZMMS 選項
class ZmmsOption(models.Model):
    description = models.CharField(max_length=36, null=False, blank=False)
    invalid = models.BooleanField(default=False)

    def __str__(self):
        return self.description

#物料控制員 選項
class MaterialCtrlOption(models.Model):
    description = models.CharField(max_length=36, null=False, blank=False)
    invalid = models.BooleanField(default=False)

    def __str__(self):
        return self.description
