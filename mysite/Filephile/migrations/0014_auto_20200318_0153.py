# Generated by Django 3.0.4 on 2020-03-18 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Filephile', '0013_auto_20200318_0145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='users',
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(to='Filephile.Group'),
        ),
    ]
