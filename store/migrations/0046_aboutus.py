# Generated by Django 3.2.15 on 2022-11-05 09:17

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0045_missionandsvision_privacypolicy_returns_policy_shippinganddelivery_termsandconditions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_information', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
