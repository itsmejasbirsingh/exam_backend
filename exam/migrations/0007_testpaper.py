# Generated by Django 4.1.6 on 2023-02-08 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_alter_question_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testpaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField(null=True)),
                ('question', models.ManyToManyField(to='exam.question')),
            ],
        ),
    ]