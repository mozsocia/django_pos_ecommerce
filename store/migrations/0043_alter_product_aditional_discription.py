# Generated by Django 3.2.15 on 2022-10-27 08:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0042_alter_product_sort_discription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='aditional_discription',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
