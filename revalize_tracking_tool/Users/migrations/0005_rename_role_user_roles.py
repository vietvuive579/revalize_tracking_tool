# Generated by Django 4.0.3 on 2022-06-10 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_alter_user_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='role',
            new_name='roles',
        ),
    ]
