# Generated by Django 3.0.4 on 2020-03-19 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Filephile', '0022_auto_20200319_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='permission_key',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]