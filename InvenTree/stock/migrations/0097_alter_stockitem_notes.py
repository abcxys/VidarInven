# Generated by Django 3.2.18 on 2023-04-19 00:37

import InvenTree.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0096_auto_20230330_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockitem',
            name='notes',
            field=InvenTree.fields.InvenTreeNotesField(blank=True, help_text='Markdown notes (optional)', max_length=50000, null=True, verbose_name='Notes'),
        ),
    ]
