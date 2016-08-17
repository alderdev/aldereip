from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from datetime import date
from django.utils import timezone
from django.db import models

from ship.models import Customer
from basic.models import Product,OrderCategory, ZmmsOption, MaterialCtrlOption

class WorkOrder(models.Model):
    category = models.ForeignKey(OrderCategory, limit_choices_to={'invalid': False} )
    zmms = models.ForeignKey(ZmmsOption, blank=True, null=True) #models.CharField(max_length=30, blank=True, null=True)
    recevice_date = models.DateField(default=timezone.now) #models.DateField(auto_now_add =True) #  收單日
    material_ctrl = models.ForeignKey(MaterialCtrlOption, blank=True, null=True) #models.CharField(max_length=30, blank=True, null=True) #物料控管
    ships_order = models.CharField(max_length=16, null=True, blank=True) # SAP訂單號碼
    customer = models.ForeignKey(Customer) #客戶編號
    work_order = models.CharField(max_length=16, null=False, blank=False, unique=True) # SAP工單號碼
    product = models.ForeignKey(Product) #  SAP料號
    ord_amount = models.IntegerField(default=1, blank=False, null=False) # 數量
    deliverly = models.DateField(blank=True, null=True) #  業務交期
    material_ready_date = models.DateField(blank=True, null=True) #  齊料日
    estimated_finish = models.DateField(blank=True, null=True) # 預計完工日
    reuqest_user = models.CharField(max_length=16, null=False, blank=False) # 申請人
    material_duty = models.CharField(max_length=16, null=False, blank=False) # 備料人
    #comfirm = models.CharField(max_length=30,blank=True, null=True) # 確認
    manage_memo = models.TextField(blank=True, null=True) # 生管備註

    create_at = models.DateTimeField(auto_now_add=True, auto_now =False)
    modify = models.DateTimeField(auto_now_add=False, auto_now =True)
