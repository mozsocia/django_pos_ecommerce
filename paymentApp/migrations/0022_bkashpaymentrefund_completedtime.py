# Generated by Django 3.2.15 on 2022-12-12 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentApp', '0021_auto_20221212_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='bkashpaymentrefund',
            name='completedTime',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]