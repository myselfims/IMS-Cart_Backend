# Generated by Django 4.2.2 on 2023-06-23 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_address_mobile_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]