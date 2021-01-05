from django.shortcuts import render,HttpResponse
import datetime
from datetime import date
from hotelbooking.models import Customer,Room,AccessRecord
from . import forms

# Create your views here.
# def Hello1(request):
#     return  HttpResponse ("Hello!!! This is my first application")
def index(request):
    today = datetime.datetime.now().date()  
    x = datetime.datetime.now() 
    m=x.strftime("%m")
    d=x.strftime("%m")
    f_date = date(x.year, int(m), int(d))
    l_date = date(x.year, 12, 10)
    # l_date = date(x.year, 4, 10)
    delta = l_date - f_date
    rem=delta.days
    dict={'today':today,'rem':rem}
    return render(request, 'hotelbooking1/index.html',context=dict)

def mvt(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records":webpages_list}
    return render(request, 'hotelbooking1/mvt.html',date_dict)

def form1(request):
    form=forms.FormName()
    if request.method=='POST':
        form=forms.FormName(request.POST)
    if form.is_valid():
        print("Validation Successful !!!")
        print("NAME:"+form.cleaned_data['name'])
        print("EMAIL:"+form.cleaned_data['email'])
        print("QUERY:"+form.cleaned_data['query'])
    return render(request, 'hotelbooking1/form.html',{'form':form})
