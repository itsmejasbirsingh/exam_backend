# Generated by Django 4.1.6 on 2023-02-15 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0015_remove_testpaper_user_testpaperassign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testpaperassign',
            name='end_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='testpaperassign',
            name='start_at',
            field=models.DateTimeField(null=True),
        ),
    ]
