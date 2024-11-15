# Generated by Django 5.1.3 on 2024-11-15 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_statistics_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Created_news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_news', models.ForeignKey(default='created_news', on_delete=django.db.models.deletion.CASCADE, to='main.news')),
            ],
        ),
    ]
