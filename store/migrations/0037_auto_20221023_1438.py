# Generated by Django 3.2.15 on 2022-10-23 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0036_auto_20221023_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='due_amount',
            field=models.CharField(default=0, max_length=150),
        ),
        migrations.AlterField(
            model_name='order',
            name='paid_amount',
            field=models.CharField(default=0, max_length=150),
        ),
    ]
