# Generated by Django 3.2.15 on 2022-10-27 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0043_alter_product_aditional_discription'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_range', models.CharField(max_length=100, unique=True)),
                ('ordering', models.IntegerField()),
            ],
            options={
                'verbose_name': 'PriceRange',
                'verbose_name_plural': 'PriceRange',
                'ordering': ['ordering'],
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='label',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sale_type',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('pending', 'pending'), ('processing', 'processing'), ('on the way', 'on the way'), ('complete', 'complete'), ('cancel', 'cancel')], default='pending', max_length=150),
        ),
        migrations.AddField(
            model_name='product',
            name='price_range',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.pricerange'),
        ),
    ]
