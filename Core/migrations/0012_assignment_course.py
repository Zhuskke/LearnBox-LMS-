# Generated by Django 4.2.6 on 2023-11-15 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0011_alter_assignment_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Core.course'),
            preserve_default=False,
        ),
    ]
