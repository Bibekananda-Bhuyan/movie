# Generated by Django 3.1 on 2020-08-22 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moviehalls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_name', models.CharField(default='', max_length=100)),
                ('hall_location', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
