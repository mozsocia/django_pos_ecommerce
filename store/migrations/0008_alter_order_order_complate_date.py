# Generated by Django 3.2 on 2022-06-14 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20220614_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_complate_date',
            field=models.DateTimeField(),
        ),
    ]
