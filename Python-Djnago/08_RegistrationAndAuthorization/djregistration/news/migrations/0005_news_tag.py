# Generated by Django 4.0.4 on 2022-04-16 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_news_tag_tags_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.CharField(default=0, help_text='tags with space', max_length=10),
            preserve_default=False,
        ),
    ]
