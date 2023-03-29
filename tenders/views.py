from django.shortcuts import render, HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Tenders
import os
from pdfrw import PdfReader
from django.http import Http404
from PyPDF2 import PdfFileReader
from io import BytesIO
from django.conf import settings
import requests
from base64 import b64encode
from tradeauxgroup.settings import consumer_key, consumer_secret
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
shortcode = 174379
import base64








# Create your views here.


class index(ListView):
    model = Tenders
    template_name = 'tenders/index.html'
    context_object_name = 'tenders'

class tender_details(DetailView):
    model = Tenders
    context_object_name = 'tenders'
    template_name = 'tenders/tenders_detail.html'

def initiate_payment(request):
    if request.method == 'POST':
        # Get form data
        amount = request.POST.get('amount')
        phone_number = request.POST.get('phone_number')
        

        # Get an OAuth access token
        url = "https://sandbox.safaricom.co.ke/oauth/v1/generate"
        querystring = {"grant_type": "client_credentials"}

        credentials = f"{consumer_key}:{consumer_secret}"
        credentials_b64 = base64.b64encode(credentials.encode("ascii")).decode("ascii")

        headers = {"Authorization": f"Basic {credentials_b64}"}

        response = requests.request("GET", url, headers=headers, params=querystring)

        response_json = response.json()
        access_token = response_json["access_token"]


        # Make M-Pesa payment request
        passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
        password = base64.b64encode(f"{shortcode}{passkey}{timestamp}".encode("ascii")).decode("ascii")
        
       
        
        url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json'
        }
       
        payload = {
            'BusinessShortCode': shortcode,
            'Password': password,
            'Timestamp': timestamp,
            'TransactionType': 'CustomerPayBillOnline',
            'Amount': 1,
            'PartyA': phone_number,
            'PartyB': 174379,
            'PhoneNumber': phone_number,
            'CallBackURL': 'https://2570-197-232-61-204.in.ngrok.io/tenders/payment_push/',
            'AccountReference': 'conference',
            'TransactionDesc': 'ticket',
        }

        response = requests.post(url, headers=headers, json=payload)
      
       # Check payment status and redirect to appropriate view
       # Check payment status and redirect to appropriate view
        if response.status_code == 200:
            response_json = response.json()
            print(response_json)
            if response_json["ResponseCode"] == "0":
                return redirect('payment_push')
            else:
                return redirect('payment_fail')
        else:
        
         return render(request, 'payment/payment_error.html', {'error_message': 'HTTP Error: {}'.format(response.status_code)})
    return render(request, 'tenders/tenders_detail.html')
    
@csrf_exempt
def payment_push(request):
    if request.method == 'POST':
        # Process the response data
        response_data = request.POST
        print(response_data)

    return render(request, 'tenders/payment_push.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve the Tenders object for the current view
        tender = self.get_object()

        # Retrieve the path to the PDF file
        pdf_path = tender.tender_file.path

        # Open the PDF file as a binary file
        with open(pdf_path, 'rb') as pdf_file:
            # Read the contents of the file
            pdf_content = pdf_file.read()

        # Add the PDF content to the context
        context['pdf_content'] = pdf_content

        return context