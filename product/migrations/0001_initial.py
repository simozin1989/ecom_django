# Generated by Django 3.2.8 on 2021-10-09 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDName', models.CharField(max_length=100, verbose_name='Product Name ')),
                ('PRDDesc', models.TextField(verbose_name='Description')),
                ('PRDImage', models.ImageField(blank=True, null=True, upload_to='prodcut/', verbose_name='Image')),
                ('PRDPrice', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('PRDDiscountPrice', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Discount Price')),
                ('PRDCost', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Cost')),
                ('PRDCreated', models.DateTimeField(verbose_name='Created At')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDIImage', models.ImageField(upload_to='prodcut/', verbose_name='Image')),
                ('PRDIProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Product')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Alternative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PALNAlternatives', models.ManyToManyField(related_name='alternative_products', to='product.Product', verbose_name='Alternatives')),
                ('PALNProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_prodcut', to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product Alternative',
                'verbose_name_plural': 'Product Alternatives',
            },
        ),
        migrations.CreateModel(
            name='Product_Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PACCAlternatives', models.ManyToManyField(related_name='accessories_products', to='product.Product', verbose_name='Accessories')),
                ('PACCProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mainAccessory_prodcut', to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product Accessory',
                'verbose_name_plural': 'Product Accessories',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATName', models.CharField(max_length=50, verbose_name='Name')),
                ('CATDesc', models.TextField(verbose_name='Description')),
                ('CATImg', models.ImageField(upload_to='category/', verbose_name='Image')),
                ('CATParent', models.ForeignKey(blank=True, limit_choices_to={'CATParent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Main Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]