# Generated by Django 4.0.3 on 2022-04-07 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('context', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'published')], max_length=2)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'db_table': 'News',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('comment', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app_news.news')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
