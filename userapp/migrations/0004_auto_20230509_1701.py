# Generated by Django 3.2.15 on 2023-05-09 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_auto_20230509_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='admin',
            new_name='is_admin',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='super_admin',
            new_name='is_super_admin',
        ),
    ]
