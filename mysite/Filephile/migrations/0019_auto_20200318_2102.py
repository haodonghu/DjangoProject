# Generated by Django 3.0.4 on 2020-03-18 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Filephile', '0018_auto_20200318_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Filephile.Group'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='manager',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Filephile.User'),
        ),
    ]
