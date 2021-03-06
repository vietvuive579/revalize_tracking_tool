# Generated by Django 4.0.3 on 2022-05-30 09:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetracking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('release', models.CharField(max_length=128)),
                ('task_id', models.CharField(max_length=128)),
                ('task_link', models.CharField(max_length=128)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=128)),
                ('note', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.UUIDField(default=uuid.uuid4)),
                ('modified_by', models.UUIDField(default=uuid.uuid4)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timetracking', to='Users.user')),
            ],
        ),
    ]
