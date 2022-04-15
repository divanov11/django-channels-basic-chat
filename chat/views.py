from django.shortcuts import render
from .models import *
# Create your views here.

def lobby(request):
    return render(request, 'chat/lobby.html')

def invoiceData(request):
    if request.POST:
        name        = request.POST['name'] 
        gstno       = request.POST['gst'] 
        hsncode     = request.POST['hsn'] 
        buyername   = request.POST['buyer']
        
        print(f"{name} : {gstno} : {hsncode} : {buyername}")
    return render(request, 'chat/invoicedata.html')