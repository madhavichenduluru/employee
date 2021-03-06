# Generated by Django 3.2.12 on 2022-03-17 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empapp', '0002_alter_employee_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaveid', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('reason', models.CharField(max_length=100)),
                ('file_name', models.CharField(max_length=255)),
                ('my_file', models.FileField(upload_to='')),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='empapp.employee')),
            ],
        ),
    ]
