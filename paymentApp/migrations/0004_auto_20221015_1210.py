# Generated by Django 3.2.15 on 2022-10-15 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentApp', '0003_auto_20221015_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipingaddress',
            name='address_location',
        ),
        migrations.AddField(
            model_name='shipingaddress',
            name='inside_chittagong',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shipingaddress',
            name='outside_chittagong',
            field=models.BooleanField(default=False),
        ),
    ]
