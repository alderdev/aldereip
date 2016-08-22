from django.db import models

# Create your models here.

#料品分類：成品 半成品
class ProductCategory(models.Model):
    description = models.CharField(max_length=36, null=False, blank=False)
    invalid = models.BooleanField(default=False)

    def __str__(self):
        return self.description

#料品生命週期狀態： 停產 量產中
class CycleStatus(models.Model):
    description = models.CharField(max_length=36, null=False, blank=False)
    invalid = models.BooleanField(default=False)

    def __str__(self):
        return self.description

#料品
class Product(models.Model):
    sap_no = models.CharField(primary_key=True, max_length=36) # SAP料號
    product_desc = models.CharField(max_length=36, null=False, blank=False) # 品名
    specification = models.CharField(max_length=100, null=True, blank=True) # 規格
    image = models.ImageField( null=True, blank=True, height_field="height_field", width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory) #料品分類
    cycle_status = models.ForeignKey(CycleStatus) # 料品狀態


    create_at = models.DateTimeField(auto_now_add=True, auto_now =False) #
    modify = models.DateTimeField(auto_now_add=False, auto_now =True) #

    def __str__(self):
        return ("%s : %s" % (self.sap_no,self.product_desc ) )


    def get_absoulte_url(self):
        return "/product/detail/%s/" %( str(self.sap_no) )
