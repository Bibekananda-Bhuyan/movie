# Generated by Django 3.1 on 2020-08-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainwebsite', '0011_event_booked_by_user_order_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='News_letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=100)),
                ('date_creattion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
