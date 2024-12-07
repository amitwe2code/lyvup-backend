# Generated by Django 5.1.3 on 2024-11-21 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('team_leader_id', models.CharField(default='amit', max_length=100)),
                ('phone', models.IntegerField(default=5)),
                ('password', models.CharField(max_length=255)),
                ('user_type', models.CharField(choices=[('Superadmin', 'Superadmin'), ('Patient', 'Patient'), ('Healthcare Provider', 'Healthcare Provider'), ('Teamlead', 'Teamlead'), ('Friend', 'Friend')], max_length=50)),
                ('profile_picture', models.CharField(blank=True, null=True)),
                ('language_preference', models.CharField(blank=True, max_length=10, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Suspended', 'Suspended')], default='Active', max_length=50)),
                ('is_team_leader', models.BooleanField(default=False)),
                ('wly_token', models.BooleanField(default=False)),
                ('is_used_token', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account', to='account.accountmodel')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
