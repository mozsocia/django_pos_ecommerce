# Generated by Django 3.2.15 on 2022-11-17 07:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0056_remove_product_sort_discription'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sort_discription',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
