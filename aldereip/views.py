from django.shortcuts import render

# Create your views here.
def alderhome(request):
    title = "亞德光機內部網站首頁"
    return render(request, "index.html", locals())
