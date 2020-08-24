# Generated by Django 3.1 on 2020-08-22 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainwebsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allowscreens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='moviehalls',
            name='hall_total_Screens',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='moviehalls',
            name='hall_avaliable_screen_type',
            field=models.ManyToManyField(default='', to='mainwebsite.Allowscreens'),
        ),
    ]