# Generated by Django 5.0.6 on 2024-05-12 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getRatings', '0003_alter_ratings_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratings',
            name='appName',
            field=models.TextField(default='unknown', max_length=20),
        ),
    ]
