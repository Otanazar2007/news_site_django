# Generated by Django 5.1.3 on 2024-11-15 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_commentary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_of_news', to='main.news')),
                ('news_url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='url_news', to='main.news')),
            ],
        ),
    ]