# Generated by Django 2.2.14 on 2021-01-14 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20201230_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formpage',
            name='from_address',
        ),
        migrations.RemoveField(
            model_name='formpage',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='formpage',
            name='to_address',
        ),
    ]