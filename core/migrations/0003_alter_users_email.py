# Generated by Django 5.2.1 on 2025-05-23 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_users_perewaladd_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
