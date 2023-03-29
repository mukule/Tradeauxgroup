from django.db import models
from django.conf import settings
import os
import uuid




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
