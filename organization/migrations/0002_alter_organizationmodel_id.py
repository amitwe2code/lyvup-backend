# Generated by Django 4.2.17 on 2024-12-21 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]