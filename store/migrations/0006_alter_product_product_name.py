# Generated by Django 3.2 on 2022-06-13 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20220613_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100),
        ),
    ]
