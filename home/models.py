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

#>Sections

#Block to display a short introduction of myself
class _S_AboutBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    name = blocks.CharBlock()
    description = blocks.RichTextBlock()
    picture = ImageChooserBlock()

    graphql_fields = [
        GraphQLString('title'),
        GraphQLString('name'),
        GraphQLString('description'),
        GraphQLImage('picture'),
    ]

#Block to display screenshots of each project
class _S_Projects_Project_ImageBlock(blocks.StructBlock):
    screenshot = ImageChooserBlock()

    graphql_fields = [
        GraphQLImage('screenshot'),
    ]


#Block to display a single project
class _S_Projects_ProjectBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    description = blocks.RichTextBlock()
    gallery = blocks.StreamBlock([
        ('screenshot', _S_Projects_Project_ImageBlock())
    ])

    graphql_fields = [
        GraphQLString('title'),
        GraphQLString('description'),
        GraphQLStreamfield('gallery'),
    ]

#Block to display the projects
class _S_ProjectsBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    projects = blocks.StreamBlock([
        ('project', _S_Projects_ProjectBlock()),
    ])

    graphql_fields = [
        GraphQLString('title'),
        GraphQLStreamfield('projects'),
    ]

class HomePage(Page):
    sections = StreamField([
        ("about", _S_AboutBlock(null=True, blank=False)),
        ("projects", _S_ProjectsBlock(null=True, blank=False)),
    ], null=True, blank=False)

    content_panels = Page.content_panels + [
        StreamFieldPanel('sections'),
    ]
    
    graphql_fields = [
        GraphQLStreamfield("sections"),
    ]
