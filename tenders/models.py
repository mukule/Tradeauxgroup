from django.db import models
from django.conf import settings
import os
import uuid
from django.contrib.auth.models import User




# Create your models here.

def pdf_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('tenders', filename)

class Tenders(models.Model):
    tender_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    tender_file = models.FileField(upload_to=pdf_upload_path)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tender = models.ForeignKey(Tenders, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=20)
    mpesa_receipt_number = models.CharField(max_length=50)
    transaction_date = models.DateTimeField(auto_now_add=True)
