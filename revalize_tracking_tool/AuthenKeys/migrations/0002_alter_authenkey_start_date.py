# Generated by Django 4.0.3 on 2022-06-16 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenKeys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authenkey',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]