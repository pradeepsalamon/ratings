# Generated by Django 5.0.6 on 2024-05-08 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getRatings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratings',
            old_name='integer_field',
            new_name='rate',
        ),
    ]
