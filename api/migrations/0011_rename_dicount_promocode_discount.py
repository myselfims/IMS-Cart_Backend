# Generated by Django 4.2.2 on 2023-06-28 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_promocode_alter_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promocode',
            old_name='dicount',
            new_name='discount',
        ),
    ]