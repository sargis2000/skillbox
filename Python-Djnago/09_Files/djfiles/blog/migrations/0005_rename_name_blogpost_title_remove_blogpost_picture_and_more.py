# Generated by Django 4.0.4 on 2022-04-18 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='picture',
        ),
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to='media/pictures/%Y%m%d', verbose_name='Picture'),
        ),
    ]
