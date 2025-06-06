# Generated by Django 5.2.1 on 2025-05-19 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summer', models.CharField(blank=True, max_length=20)),
                ('winter', models.CharField(blank=True, max_length=20)),
                ('autumn', models.CharField(blank=True, max_length=20)),
                ('spring', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('family', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('otc', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='PerewalAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('other_title', models.CharField(max_length=100)),
                ('connect', models.CharField(blank=True, max_length=100, null=True)),
                ('add_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('new', 'Новый'), ('pending', 'В обработке'), ('accepted', 'Принятый'), ('rejected', 'Отклоненный')], default='new', max_length=20)),
                ('coords', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.coords')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.level')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.users')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
                ('title', models.CharField(max_length=255)),
                ('perewal_added', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.perewaladd')),
            ],
        ),
    ]
