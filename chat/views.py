from django.shortcuts import render
from .models import *
# Create your views here.

def lobby(request):
    return render(request, 'chat/lobby.html')

def ledgerData(request):
    if request.POST:
        name        = request.POST['name'] 
        gstno       = request.POST['gst'] 
        hsncode     = request.POST['hsn'] 
        buyername   = request.POST['buyer']
        pdf_details.objects.create(name=name, gstno=gstno,hsncode=hsncode,buyername=buyername)
        # print(f"{name} : {gstno} : {hsncode} : {buyername}")
    return render(request, 'chat/ledgerData.html')

def voucherData(request):
    if request.POST:
        name        = request.POST['name'] 
        gstno       = request.POST['gst'] 
        hsncode     = request.POST['hsn'] 
        pdf_details.objects.create(name=name, gstno=gstno,hsncode=hsncode)
        # print(f"{name} : {gstno} : {hsncode}")
    return render(request, 'chat/voucherData.html')

def invoiceData(request):
    if request.POST:
        name        = request.POST['name'] 
        gstno       = request.POST['gst'] 
        pdf_details.objects.create(name=name, gstno=gstno)
        # print(f"{name} : {gstno}")
    return render(request, 'chat/invoiceData.html')



