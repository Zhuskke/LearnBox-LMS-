# Generated by Django 4.2.6 on 2023-11-15 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0012_assignment_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='duration',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateTimeField(),
        ),
    ]
