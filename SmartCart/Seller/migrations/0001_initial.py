# Generated by Django 5.1.6 on 2025-02-19 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Administrator', '0001_initial'),
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.CharField(max_length=50)),
                ('product_details', models.CharField(max_length=50)),
                ('product_photo', models.FileField(upload_to='Assets/ProductPhoto/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.tbl_brandname')),
                ('sellerID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_seller')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.tbl_subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_productimages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_details', models.CharField(max_length=50)),
                ('productimage_photo', models.FileField(upload_to='Assets/GallaryPhoto/')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Seller.tbl_product')),
            ],
        ),
    ]
