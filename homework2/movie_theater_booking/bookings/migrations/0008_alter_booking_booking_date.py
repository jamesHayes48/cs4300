# Generated by Django 4.2.11 on 2025-02-28 20:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_alter_seat_seat_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default=datetime.date(2025, 2, 28)),
        ),
    ]
