# Generated by Django 3.2.18 on 2023-05-13 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0064_move_address_field_to_address_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='address',
        ),
    ]
