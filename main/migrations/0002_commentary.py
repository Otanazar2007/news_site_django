# Generated by Django 5.1.3 on 2024-11-15 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('comm', models.TextField(max_length=150)),
                ('comm_photo', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('news_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaries', to='main.news')),
                ('urls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='url_commentaries', to='main.news')),
            ],
            options={
                'verbose_name': 'Добавить комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
