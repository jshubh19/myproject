# Generated by Django 2.0 on 2018-01-26 19:42

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_student'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='publisher',
            managers=[
                ('pub', django.db.models.manager.Manager()),
            ],
        ),
    ]
