# Generated by Django 4.0.4 on 2022-04-16 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_remove_tags_news_tags_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='news',
        ),
        migrations.AlterField(
            model_name='news',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.tags'),
        ),
    ]
