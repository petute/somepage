from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import StreamFieldPanel

from grapple.helpers import register_streamfield_block

from grapple.models import (
    GraphQLStreamfield,
    GraphQLImage,
    GraphQLString,
)

#Sections

#Block to display a short introduction of myself

class _S_AboutBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    name = blocks.CharBlock()
    description = blocks.RichTextBlock()
    picture = ImageChooserBlock()

    graphql_fields = [
        GraphQLString('name'),
        GraphQLString('description'),
        GraphQLImage('picture'),
    ]

#Block to display the projects I was involve in

class _S_ProjectsBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    projects = StreamField([
        ('project', _S_Projects_PorjectBlock()),
    ])

class HomePage(Page):
    pass
