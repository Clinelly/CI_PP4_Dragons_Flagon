# Generated by Django 3.2.16 on 2023-03-04 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_rename_date_tablebooking_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tablebooking',
            old_name='name',
            new_name='user',
        ),
    ]
