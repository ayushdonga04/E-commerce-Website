# Generated by Django 5.0.7 on 2024-09-19 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecap', '0002_regestration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regestration',
            name='password',
            field=models.CharField(max_length=8),
        ),
    ]
