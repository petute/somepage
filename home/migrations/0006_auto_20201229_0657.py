# Generated by Django 2.2.14 on 2020-12-29 06:57

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_formfield_formpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formpage',
            name='intro',
        ),
        migrations.AlterField(
            model_name='formfield',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_form_fields', to='home.FormPage'),
        ),
    ]
