# Generated by Django 5.1.1 on 2024-10-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecap', '0013_product_delete_vendor_show'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.PositiveIntegerField(unique=True)),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('sale_date', models.DateField()),
                ('product_name', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gst_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('gst_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
