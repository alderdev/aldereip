from django.db import models

# Create your models here.



class CycleStatus(models.Model):
    description = models.CharField(max_length=36, null=False, blank=False)
    invalid = models.BooleanField(default=False)

    def __str__(self):
        return self.description


class Product(models.Model):
    sap_no = models.CharField(max_length=36, null=False, blank=False) # SAP料號
    product_desc = models.CharField(max_length=36, null=False, blank=False) # 品名
    specification = models.CharField(max_length=100, null=False, blank=False) # 規格
    cycle_status = models.ForeignKey(CycleStatus) # 料品狀態
    create_at = models.DateTimeField(auto_now_add=True, auto_now =False) #
    modify = models.DateTimeField(auto_now_add=False, auto_now =True) #

    def __str__(self):
        return ("%s : %s" % (self.sap_no,self.product_desc ) )
