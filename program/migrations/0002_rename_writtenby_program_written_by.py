# Generated by Django 4.2.17 on 2025-01-01 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='writtenby',
            new_name='written_by',
        ),
    ]
