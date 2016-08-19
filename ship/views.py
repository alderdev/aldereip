from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone

from .models import QuoteHead, Customer
from .forms import QuoteHeadCreateForm, QuoteLineCreateForm

# Create your views here.
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.colors import pink, green, brown, white, black, blue
def export_pdf(request):

    # Create the HttpResponse object with the appropriate PDF headers.


    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Quotetion.pdf"'

    # Create the PDF object, using the response object as its "file."
    record = get_object_or_404( QuoteHead, id=1)
    print( dir( record ))
    '''
    request_user = models.CharField(max_length=60, null=False, blank=False) #開單人
    order_number = models.IntegerField(null=True, blank=True, unique=True) #報價單號
    ord_date = models.DateField(default=timezone.now) #報價日期
    customer = models.ForeignKey(Customer) #客戶編號
    effective_date = models.DateField( default=timezone.now ) # 報價單有效日期
    currency = models.ForeignKey( Currency )
    invalid = models.BooleanField(default=False) #作廢
    memo = models.TextField(null=True, blank=True)
    '''

    p = canvas.Canvas(response)
    date, *_ = str(timezone.now()).split(' ')


    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    #seal = '/static/img/alder_logo.png'
    #p.drawImage(seal, 210,800, width=None, height=None)

    p.setFont('Helvetica', 20)
    p.drawCentredString(310, 810, "Alder Optomechanical Corp.")
    p.setFont('Helvetica', 16)
    p.drawCentredString(310, 795, "Quotetion")
    p.setFont('Helvetica', 10)
    p.drawRightString( 580, 810 , "Print Date: " + date)


    
    p.drawRightString( 150, 660 , "Sales Name:"  )
    p.drawRightString( 150, 650 , "Order Number:" )
    p.drawRightString( 150, 640 , "Order Date:"  )
    p.drawRightString( 150, 630 , "Effective Date:" )
    p.drawRightString( 150, 620 , "Currency:"  )
    p.drawRightString( 150, 610 , "Comment:"  )

    p.drawString( 160, 660 , record.request_user )
    p.drawString( 160, 650 ,  str(record.order_number))
    p.drawString( 160, 640 ,  str(record.ord_date) )
    p.drawString( 160, 630 ,  str(record.effective_date))
    p.drawString( 160, 620 ,  str(record.currency) )
    p.drawString( 160, 610 ,  str(record.memo) )



    '''
    p.setFont('Helvetica', 10)
    p.drawRightString( 580, 610 , date)
    p.setFillColor(blue)

    p.setTitle("QUOTATION")
    y = 780
    for font in p.getAvailableFonts():
        y-=10
        p.drawRightString(150, y, font+":") # 向右對齊
        p.drawCentredString(150, y, font+":") # 置中對齊
    p.drawString(190, 780, "Hello World")
    '''
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response






def ship_list(request):
    title = "銷售管理"

    queryset_list = QuoteHead.objects.all()

    paginator = Paginator(queryset_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    return render(request, "ship_list.html", locals())


def create_quote(request):
    title = "新增報價單"
    form = QuoteHeadCreateForm(request.POST or None)

    if form.is_valid():

        instance = form.save(commit=False)
        instance.order_number = QuoteHead.objects.month_sequence()  # 自訂的單據號碼
        print(instance.order_number)
        instance.save()

        messages.success(request, "Successfully Create")
        return HttpResponseRedirect(instance.get_absoulte_url())

    return render(request, "quote_header.html", locals())


def quote_detail(request, id):
    title = "報價單明細"
    record = get_object_or_404( QuoteHead, id=id)

    form = QuoteLineCreateForm(request.POST or None )

    if form.is_valid():

        instance = form.save(commit=False)
        #print( instance.get_absoulte_url() )
        instance.save()
        messages.success(request, "Successfully Create Line")
        return HttpResponseRedirect(instance.get_absoulte_url())



    return render(request, "quote_detail.html", locals())


def quote_create_line(request):

    form = QuoteLineCreateForm(request.POST or None )
    #print( form.quotehead.id )
    if form.is_valid():

        instance = form.save(commit=False)
        #print( instance.get_absoulte_url() )
        instance.save()
        messages.success(request, "Successfully Create Line")
        return HttpResponseRedirect(instance.get_absoulte_url())

    return render(request, "quote_detail.html", locals())




# 給AJAX用來回傳客戶資料
def customer_name(request,id):

    obj = get_object_or_404( Customer, sap_no=id)
    #print(obj.title)
    return render(request, "ajax_customer.html", locals())
