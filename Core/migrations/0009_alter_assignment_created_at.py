# Generated by Django 4.2.4 on 2023-11-11 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0008_alter_assignment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 11, 16, 32, 46, 965478, tzinfo=datetime.timezone.utc)),
        ),
    ]
