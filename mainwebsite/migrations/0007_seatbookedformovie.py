# Generated by Django 3.1 on 2020-08-23 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainwebsite', '0006_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seatbookedformovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_timeslots', models.CharField(default='', max_length=100)),
                ('seat_no', models.CharField(default='', max_length=100)),
                ('booked_time', models.DateTimeField(auto_now_add=True)),
                ('selected_movie', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mainwebsite.movie')),
                ('selected_movie_hall', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mainwebsite.moviehalls')),
            ],
        ),
    ]
