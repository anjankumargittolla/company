# Generated by Django 3.2.3 on 2021-05-27 06:49

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
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=25)),
                ('team_members', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='job.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=20)),
                ('emp_email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default=None, max_length=8)),
                ('profile_pic', models.ImageField(upload_to='', verbose_name='media/')),
                ('phone', models.IntegerField()),
                ('qualification', models.CharField(max_length=20)),
                ('experience', models.IntegerField(default=0)),
                ('is_verified', models.BooleanField(default=False)),
                ('designation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='emp_role', to='job.designation')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('teams', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='job.team')),
            ],
        ),
        migrations.CreateModel(
            name='MailBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('body', models.TextField(max_length=500)),
                ('files', models.FileField(upload_to='', verbose_name='media/')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='job.employee')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='job.employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_details',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='job.register'),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
