# Generated by Django 4.0.5 on 2022-06-19 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hood', '0009_alter_admin_username_alter_neighbourhood_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='confirm_password',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='email',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='password',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='confirm_password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AddField(
            model_name='admin',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]