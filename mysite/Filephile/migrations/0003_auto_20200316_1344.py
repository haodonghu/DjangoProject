# Generated by Django 3.0.4 on 2020-03-16 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filephile', '0002_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='Data',
            new_name='data',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='File_Name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='file',
            name='Date_Added',
        ),
        migrations.RemoveField(
            model_name='file',
            name='Desciption',
        ),
        migrations.RemoveField(
            model_name='file',
            name='Owner',
        ),
    ]