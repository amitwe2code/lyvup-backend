# Generated by Django 5.1.3 on 2025-01-02 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0011_alter_intervention_activity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervention',
            name='duration_coach',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='user_duration',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
