# Generated by Django 4.1.6 on 2023-02-08 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_testpaper'),
    ]

    operations = [
        migrations.AddField(
            model_name='testpaper',
            name='time',
            field=models.IntegerField(default=30, help_text='time in minutes'),
        ),
        migrations.AlterField(
            model_name='testpaper',
            name='title',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
