# Generated by Django 4.2.2 on 2023-06-23 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='mobile',
            field=models.CharField(default='233432', max_length=10),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
