# Generated by Django 4.2.4 on 2023-11-11 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Announcements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='content',
            field=models.TextField(max_length=500),
        ),
    ]
