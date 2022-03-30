# Generated by Django 3.2.12 on 2022-03-14 17:43

import app_users.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_Pic', models.ImageField(blank=True, upload_to=app_users.models.path_and_rename, verbose_name='Profile Picture')),
                ('user_type', models.CharField(choices=[('user1', 'user1'), ('user2', 'user2')], default='user1', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]