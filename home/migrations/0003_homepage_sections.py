# Generated by Django 2.2.14 on 2020-07-15 19:42

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='sections',
            field=wagtail.core.fields.StreamField([('about', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('name', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.RichTextBlock()), ('picture', wagtail.images.blocks.ImageChooserBlock())], blank=False, null=True)), ('projects', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock())], blank=False, null=True))], null=True),
        ),
    ]
