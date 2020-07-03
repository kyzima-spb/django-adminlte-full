# Generated by Django 3.0.5 on 2020-07-03 14:14

import adminlte_base.mixins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('program_name', models.CharField(max_length=255, unique=True)),
            ],
            bases=(models.Model, adminlte_base.mixins.MenuMixin),
        ),
        migrations.CreateModel(
            name='MenuItemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('link', 'Link'), ('header', 'Header'), ('dropdown divider', 'Dropdown Divider')], default='link', max_length=20)),
                ('title', models.CharField(max_length=500)),
                ('url', models.URLField(blank=True, max_length=500)),
                ('endpoint', models.CharField(blank=True, max_length=255)),
                ('endpoint_args', models.TextField(blank=True)),
                ('endpoint_kwargs', models.TextField(blank=True)),
                ('icon', models.CharField(blank=True, max_length=50)),
                ('help', models.CharField(blank=True, max_length=500)),
                ('pos', models.IntegerField(blank=True, default=0)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adminlte_full.MenuModel')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='adminlte_full.MenuItemModel')),
            ],
            bases=(models.Model, adminlte_base.mixins.MenuItemMixin),
        ),
    ]
