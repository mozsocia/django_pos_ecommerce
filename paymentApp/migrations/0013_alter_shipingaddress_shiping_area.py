# Generated by Django 3.2.15 on 2022-10-18 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentApp', '0012_alter_shipingaddress_shiping_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipingaddress',
            name='shiping_area',
            field=models.CharField(choices=[('Inside Dhaka', 'Inside Dhaka'), ('Outside Dhaka', 'Outside Dhaka'), ('Only Chittagong District', 'Only Chittagong District')], max_length=100),
        ),
    ]
