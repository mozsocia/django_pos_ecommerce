# Generated by Django 3.2.15 on 2023-06-14 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos_dashboard', '0002_auto_20230612_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('customer_ID', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('start_date', models.DateField(max_length=50)),
                ('image', models.ImageField(upload_to='media/supplier_image')),
                ('Created_at', models.DateTimeField(blank=True, max_length=100, null=True)),
                ('Updated_at', models.DateTimeField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customer',
            },
        ),
        migrations.RemoveField(
            model_name='brand',
            name='Created_at',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='Updated_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='Created_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='Updated_at',
        ),
        migrations.CreateModel(
            name='Sales_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('billing_date', models.DateField()),
                ('product_code', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('unit_price', models.FloatField()),
                ('sale_price', models.FloatField()),
                ('total_price', models.FloatField()),
                ('total_descount', models.FloatField(blank=True, null=True)),
                ('sub_total', models.FloatField()),
                ('paid', models.FloatField()),
                ('due', models.FloatField(blank=True, null=True)),
                ('Created_at', models.DateTimeField(blank=True, max_length=100, null=True)),
                ('Updated_at', models.DateTimeField(blank=True, max_length=100, null=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pos_dashboard.brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pos_dashboard.category')),
                ('customer_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pos_dashboard.customer')),
                ('product_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pos_dashboard.purchase_product')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pos_dashboard.unit')),
            ],
            options={
                'verbose_name': 'Sales_Product',
                'verbose_name_plural': 'Sales_Products',
            },
        ),
    ]