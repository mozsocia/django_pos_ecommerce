# Generated by Django 3.2.15 on 2022-11-17 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0049_productpercel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.CharField(default='nocode', max_length=150),
        ),
    ]
