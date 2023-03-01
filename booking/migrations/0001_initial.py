# Generated by Django 3.2.16 on 2023-02-21 20:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TableBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('service', models.CharField(choices=[('Drinks', 'Drinks'), ('Food and Drinks', 'Food and Drinks'), ('Board Game Session', 'Board Game Session'), ('Food, Drinks and Games', 'Food, Drinks and Games')], default='Drinks', max_length=50)),
                ('phone', models.IntegerField()),
                ('Date', models.DateField(default=datetime.datetime.now)),
                ('time', models.CharField(choices=[('12 PM', '12 PM'), ('1 PM', '1 PM'), ('2 PM', '2 PM'), ('3 PM', '3 PM'), ('4 PM', '4 PM'), ('5 PM', '5 PM'), ('6 PM', '6 PM'), ('7 PM', '7 PM'), ('8 PM', '8 PM'), ('9 PM', '9 PM')], default='12 PM', max_length=10)),
                ('time_booked', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]