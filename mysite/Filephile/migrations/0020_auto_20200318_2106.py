# Generated by Django 3.0.4 on 2020-03-18 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Filephile', '0019_auto_20200318_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Filephile.User'),
        ),
    ]