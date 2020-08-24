# Generated by Django 3.1 on 2020-08-23 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainwebsite', '0009_auto_20200823_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_booked_by_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=100)),
                ('user_phone_no', models.CharField(default='', max_length=100)),
                ('user_email', models.CharField(default='', max_length=100)),
                ('Selected_Event', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mainwebsite.event')),
                ('User', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mainwebsite.users')),
            ],
        ),
    ]