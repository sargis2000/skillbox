# Generated by Django 4.0.3 on 2022-04-05 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adv',
            name='adv_price',
            field=models.FloatField(max_length=7, verbose_name='Price'),
        ),
    ]
