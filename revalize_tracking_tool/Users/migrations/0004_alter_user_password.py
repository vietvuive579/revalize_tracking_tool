# Generated by Django 4.0.3 on 2022-06-01 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]