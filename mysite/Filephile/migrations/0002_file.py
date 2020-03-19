# Generated by Django 3.0.4 on 2020-03-08 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Filephile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File_Name', models.CharField(max_length=40)),
                ('Data', models.FileField(upload_to='')),
                ('Date_Added', models.DateTimeField(auto_now_add=True)),
                ('Desciption', models.CharField(max_length=240)),
                ('Owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Filephile.User')),
            ],
        ),
    ]
