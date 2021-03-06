# Generated by Django 2.2.14 on 2020-12-30 21:05

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20201229_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='sections',
            field=wagtail.core.fields.StreamField([('about', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('name', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.RichTextBlock()), ('picture', wagtail.images.blocks.ImageChooserBlock())], blank=False, null=True)), ('projects', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('projects', wagtail.core.blocks.StreamBlock([('project', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.RichTextBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('screenshot', wagtail.core.blocks.StructBlock([('screenshot', wagtail.images.blocks.ImageChooserBlock())]))]))]))]))], blank=False, null=True)), ('footer', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('contact', wagtail.core.blocks.CharBlock())], blank=False, null=True))], null=True),
        ),
    ]
