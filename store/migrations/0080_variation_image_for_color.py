# Generated by Django 3.2.15 on 2022-12-20 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0079_auto_20221218_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='image_for_color',
            field=models.ImageField(blank=True, null=True, upload_to='ColorImage'),
        ),
    ]
