# Generated by Django 4.0.4 on 2022-04-16 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0002_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='posted_news',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
