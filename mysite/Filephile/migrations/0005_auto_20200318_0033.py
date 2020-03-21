# Generated by Django 3.0.4 on 2020-03-18 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Filephile', '0004_auto_20200316_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=40, null=True)),
                ('Date_Created', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='file',
            name='data',
            field=models.FileField(upload_to='Filephile/static/files'),
        ),
    ]