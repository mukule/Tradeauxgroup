# Generated by Django 4.1.7 on 2023-03-28 14:00

from django.db import migrations, models
import tenders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tenders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tender_name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('tender_file', models.FileField(upload_to=tenders.models.pdf_upload_path)),
            ],
        ),
    ]
