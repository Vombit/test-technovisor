# Generated by Django 4.2.5 on 2023-10-10 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corporate_food', '0007_order_dish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='dishes',
        ),
    ]