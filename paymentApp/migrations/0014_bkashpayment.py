# Generated by Django 3.2.15 on 2022-12-09 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentApp', '0013_alter_shipingaddress_shiping_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='BkashPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentID', models.CharField(max_length=150)),
                ('createTime', models.DateTimeField()),
                ('orgName', models.CharField(max_length=150)),
                ('transactionStatus', models.CharField(max_length=150)),
                ('amount', models.CharField(max_length=150)),
                ('currency', models.CharField(max_length=150)),
                ('intent', models.CharField(max_length=150)),
                ('merchantInvoiceNumber', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'BkashPayment',
                'verbose_name_plural': 'BkashPayments',
            },
        ),
    ]
