# Generated by Django 4.2.5 on 2023-10-10 12:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('corporate_food', '0005_rename_date_time_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='dishes',
            field=models.ManyToManyField(to='corporate_food.dish'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='Order_Dish',
        ),
    ]
