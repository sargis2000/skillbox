# Generated by Django 4.0.3 on 2022-04-05 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0003_alter_adv_adv_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adv',
            name='adv_price',
            field=models.FloatField(verbose_name='Price'),
        ),
    ]
