# Generated by Django 3.2.15 on 2022-09-21 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_flashsale_flashsale_expire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashsale',
            name='FlashSale_expire_date',
            field=models.DateTimeField(),
        ),
    ]
