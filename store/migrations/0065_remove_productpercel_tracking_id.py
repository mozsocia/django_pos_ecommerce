# Generated by Django 3.2.15 on 2022-11-23 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0064_auto_20221123_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpercel',
            name='tracking_id',
        ),
    ]
