# Generated by Django 4.2.5 on 2023-10-10 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corporate_food', '0004_alter_order_date_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_time',
            new_name='date',
        ),
    ]
