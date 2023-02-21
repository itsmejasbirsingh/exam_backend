# Generated by Django 4.1.6 on 2023-02-16 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exam', '0017_rename_language_course_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestpaperAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exam.option')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exam.question')),
                ('testpaperassign', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exam.testpaperassign')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]