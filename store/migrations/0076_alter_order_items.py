# Generated by Django 3.2.15 on 2022-11-26 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0075_auto_20221126_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='store.OrderItem'),
        ),
    ]
