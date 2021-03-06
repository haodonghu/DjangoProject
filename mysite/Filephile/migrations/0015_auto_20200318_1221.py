# Generated by Django 3.0.4 on 2020-03-18 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Filephile', '0014_auto_20200318_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='private',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='Date_Created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, to='Filephile.Group'),
        ),
    ]
