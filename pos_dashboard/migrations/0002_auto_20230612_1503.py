# Generated by Django 3.2.15 on 2023-06-12 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='discription',
            new_name='parent',
        ),
    ]
