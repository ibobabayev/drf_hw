# Generated by Django 5.0.4 on 2024-05-01 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_amount',
            field=models.PositiveIntegerField(verbose_name='сумма оплаты'),
        ),
    ]
