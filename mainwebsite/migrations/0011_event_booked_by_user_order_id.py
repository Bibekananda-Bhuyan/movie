# Generated by Django 3.1 on 2020-08-23 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainwebsite', '0010_event_booked_by_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_booked_by_user',
            name='Order_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
