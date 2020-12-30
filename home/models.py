from modelcluster.fields import ParentalKey

from wagtail.core import blocks
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from grapple.helpers import register_streamfield_block

from grapple.models import (
    GraphQLStreamfield,
    GraphQLImage,
    GraphQLString,
)

#>Sections

#Block to display a short introduction of myself
@register_streamfield_block
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

    class Meta:
        template = 'home/blocks/_S_About.html'

#Block to display screenshots of each project
@register_streamfield_block
class _S_Projects_Project_ImageBlock(blocks.StructBlock):
    screenshot = ImageChooserBlock()

    graphql_fields = [
        GraphQLImage('screenshot'),
    ]

    class Meta:
        template = 'home/blocks/_S_Projects_Project_Image.html'


#Block to display a single project
@register_streamfield_block
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

    class Meta:
        template = 'home/blocks/_S_Projects_Project.html'

#Block to display the projects
@register_streamfield_block
class _S_ProjectsBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    projects = blocks.StreamBlock([
        ('project', _S_Projects_ProjectBlock()),
    ])

    graphql_fields = [
        GraphQLString('title'),
        GraphQLStreamfield('projects'),
    ]

    class Meta:
        template = 'home/blocks/_S_Projects.html'

@register_streamfield_block
class _S_FooterBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    contact = blocks.CharBlock()

    graphql_fields = [
        GraphQLString('name'),
        GraphQLString('contact'),
    ]

#>Forms
class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='custom_form_fields')


class FormPage(AbstractEmailForm):
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        InlinePanel('custom_form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email Notification Config"),
    ]

    def get_form_fields(self):
        return self.custom_form_fields.all()

class HomePage(Page):
    sections = StreamField([
        ("about", _S_AboutBlock(null=True, blank=False)),
        ("projects", _S_ProjectsBlock(null=True, blank=False)),
        ("footer", _S_FooterBlock(null=True, blank=False)),
    ], null=True, blank=False)

    content_panels = Page.content_panels + [
        StreamFieldPanel('sections'),
    ]
    
    graphql_fields = [
        GraphQLStreamfield("sections"),
    ]
