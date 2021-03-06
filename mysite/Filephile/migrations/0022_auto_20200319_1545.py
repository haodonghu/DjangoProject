# Generated by Django 3.0.4 on 2020-03-19 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Filephile', '0021_auto_20200318_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Filephile.Group'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Filephile.User'),
        ),
    ]
