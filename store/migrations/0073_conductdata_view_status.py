# Generated by Django 3.2.15 on 2022-11-26 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0072_order_order_read_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='conductdata',
            name='view_status',
            field=models.BooleanField(default=False),
        ),
    ]
