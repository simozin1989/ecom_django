# Generated by Django 3.2.8 on 2021-10-11 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20211011_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='PRDIImage',
            field=models.ImageField(upload_to='images/', verbose_name='Image'),
        ),
    ]
