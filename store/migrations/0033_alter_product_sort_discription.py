# Generated by Django 3.2.15 on 2022-10-22 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0032_alter_productreview_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sort_discription',
            field=models.TextField(blank=True, null=True),
        ),
    ]
