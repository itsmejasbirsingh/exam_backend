# Generated by Django 4.1.6 on 2023-02-10 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_option_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
