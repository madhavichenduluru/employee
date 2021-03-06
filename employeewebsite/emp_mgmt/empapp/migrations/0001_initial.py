# Generated by Django 3.2.12 on 2022-03-15 08:27

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
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeid', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('position', models.CharField(max_length=50)),
                ('hiringdate', models.DateField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
