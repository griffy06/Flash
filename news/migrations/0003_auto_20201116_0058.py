# Generated by Django 2.2.2 on 2020-11-15 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_flashuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flashuser',
            name='username',
        ),
        migrations.AlterField(
            model_name='flashuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
