# Generated by Django 4.2.17 on 2024-12-31 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0010_alter_intervention_intervention_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervention',
            name='activity',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='language',
            field=models.CharField(blank=True, choices=[('english', 'english'), ('french', 'french'), ('other', 'other')], max_length=50, null=True),
        ),
    ]
