# Generated by Django 5.1.3 on 2024-11-15 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_statistics'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statistics',
            options={'verbose_name': 'Накрутить просмотры', 'verbose_name_plural': 'Просмотры'},
        ),
    ]
