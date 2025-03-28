# Generated by Django 5.1.1 on 2024-10-04 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecap', '0010_product_sale_vendor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
        migrations.AlterField(
            model_name='vendor',
            name='product_quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
