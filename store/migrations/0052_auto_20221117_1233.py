# Generated by Django 3.2.15 on 2022-11-17 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0051_alter_product_product_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='expire_date',
            new_name='flash_sale_add_and_expire_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='in_stock',
        ),
        migrations.AddField(
            model_name='product',
            name='product_purchase_price',
            field=models.IntegerField(default=5500),
        ),
    ]
