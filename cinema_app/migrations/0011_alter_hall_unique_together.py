# Generated by Django 4.1.3 on 2022-12-06 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0010_alter_hall_seats_columns_alter_hall_seats_rows'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='hall',
            unique_together={('nr', 'cinema_id')},
        ),
    ]