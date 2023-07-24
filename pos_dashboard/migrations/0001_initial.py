# Generated by Django 3.2.15 on 2023-06-12 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('discription', models.CharField(blank=True, max_length=250, null=True)),
                ('image', models.ImageField(upload_to='media/Brand_image')),
                ('Created_at', models.DateTimeField(blank=True, max_length=100, null=True)),
                ('Updated_at', models.DateTimeField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brand',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('discription', models.CharField(blank=True, max_length=250, null=True)),
                ('image', models.ImageField(upload_to='media/Category_image')),
                ('Created_at', models.DateTimeField(blank=True, max_length=100, null=True)),
                ('Updated_at', models.DateTimeField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categorys',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('supplier_type', models.CharField(max_length=100)),
                ('supplier_ID', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('start_date', models.DateField(max_length=50)),
                ('amount', models.FloatField(max_length=30)),
                ('guarantor_name', models.CharField(max_length=100)),
                ('guarantor_phone', models.IntegerField()),
                ('Chassis_no', models.CharField(max_length=30)),
                ('Transport_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media/supplier_image')),
                ('Created_at', models.DateTimeField(blank=True, max_length=100, null=True)),
                ('Updated_at', models.DateTimeField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Unit',
                'verbose_name_plural': 'Units',
            },
        ),
        migrations.CreateModel(
            name='Purchase_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('billing_date', models.DateField()),
                ('product_name', models.CharField(blank=True, max_length=100, null=True)),
                ('product_code', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField()),
                ('unit_price', models.FloatField()),
                ('buy_price', models.FloatField()),
                ('sale_price', models.FloatField()),
                ('whole_sale_price', models.FloatField()),
                ('total_price', models.FloatField()),
                ('total_descount', models.FloatField(blank=True, null=True)),
                ('sub_total', models.FloatField()),
                ('paid', models.FloatField()),
                ('due', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='media/')),
                ('Created_at', models.DateTimeField(blank=True, max_length=100, null=True)),
                ('Updated_at', models.DateTimeField(blank=True, max_length=100, null=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='pos_dashboard.brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='pos_dashboard.category')),
                ('supplier_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchase_Product', to='pos_dashboard.supplier')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unit', to='pos_dashboard.unit')),
            ],
            options={
                'verbose_name': 'Purchase_Product',
                'verbose_name_plural': 'Purchase_Products',
            },
        ),
    ]