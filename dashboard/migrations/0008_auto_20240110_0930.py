# Generated by Django 3.1.6 on 2024-01-10 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20240110_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bed',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.departments'),
        ),
    ]
