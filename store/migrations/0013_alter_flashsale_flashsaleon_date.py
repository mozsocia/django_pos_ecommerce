# Generated by Django 3.2.15 on 2022-09-20 07:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_flashsale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashsale',
            name='FlashSaleOn_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
