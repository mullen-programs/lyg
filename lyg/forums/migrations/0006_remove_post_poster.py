# Generated by Django 3.0.2 on 2020-01-29 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0005_auto_20200129_0344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='poster',
        ),
    ]
