from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone

from reportlab.pdfgen import canvas
from .models import QuoteHead, Customer
from .forms import QuoteHeadCreateForm, QuoteLineCreateForm

# Create your views here.

def export_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Quotetion.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    #seal = '/static/img/alder_logo.png'
    #p.drawImage(seal, 210,800, width=None, height=None)
    p.setFont('Helvetica', 24)
    p.drawCentredString(210, 800, "Alder Optomechanical Corp.")

    p.setFont('Helvetica', 18)
    p.drawString(190, 780, "QUOTATION")

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



    #order_number =  (int(order_date.replace('-','')[:6]) *10000)+ 1 + x

    if form.is_valid():

        order_date, _ = str(timezone.now()).split(' ')
        nextNumber = QuoteHead.objects.filter(ord_date__contains = order_date[:7] ).count()+1
        order_number = int(order_date[:7].replace('-',''))*10000
        print(order_number+nextNumber)

        #order_date = request.POST['ord_date']
        #x = QuoteHead.objects.filter(ord_date__contains = order_date.replace('/','-')[:7] ).count()
        #order_number =  (int(order_date.replace('-','')[:6]) *10000)+ 1 + x

        instance = form.save(commit=False)
        instance.order_number = order_number+nextNumber
        print(instance.order_number)
        instance.save()

        messages.success(request, "Successfully Create")
        return HttpResponseRedirect(instance.get_absoulte_url())

    return render(request, "quote_header.html", locals())


def quote_detail(request, id):
    title = "報價單明細"
    record = get_object_or_404( QuoteHead, id=id)

    form = QuoteLineCreateForm(request.POST or None )
    #print( form.quotehead.id )
    if form.is_valid():

        instance = form.save(commit=False)
        print( instance.get_absoulte_url() )
        instance.save()
        messages.success(request, "Successfully Create Line")
        return HttpResponseRedirect(instance.get_absoulte_url())



    return render(request, "quote_detail.html", locals())


def quote_create_line(request):

    form = QuoteLineCreateForm(request.POST or None )
    #print( form.quotehead.id )
    if form.is_valid():

        instance = form.save(commit=False)
        print( instance.get_absoulte_url() )
        instance.save()
        messages.success(request, "Successfully Create Line")
        return HttpResponseRedirect(instance.get_absoulte_url())

    return render(request, "quote_detail.html", locals())


















def customer_name(request,id):

    obj = get_object_or_404( Customer, sap_no=id)
    #print(obj.title)
    return render(request, "ajax_customer.html", locals())
