# Generated by Django 4.2.17 on 2025-01-01 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_alter_usermodel_is_active_alter_usermodel_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='is_active',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='is_deleted',
            field=models.IntegerField(default=0),
        ),
    ]
