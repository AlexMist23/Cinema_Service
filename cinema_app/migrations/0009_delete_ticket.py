# Generated by Django 4.1.4 on 2022-12-14 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0008_remove_ticket_user_id_ticket_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ticket',
        ),
    ]
