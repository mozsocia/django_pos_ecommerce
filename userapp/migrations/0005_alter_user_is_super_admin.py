# Generated by Django 3.2.15 on 2023-05-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_auto_20230509_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_super_admin',
            field=models.BooleanField(default=False, verbose_name='Is super admin'),
        ),
    ]
