from django.db import models

# Create your models here.
from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class ForYouPage(Page):
    """
    The 'For You' page that lists recommended spaces.

    This page acts as a container for individual space pages (child pages)
    that are recommended for users. It includes an introduction field
    that editors can use to provide context or a welcome message.
    """

    intro = RichTextField(blank=True)

    # Defines the editing interface in Wagtail's admin.
    # It extends the default content panels provided by Page with a panel
    # for editing the 'intro' field.
    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]


class SpacePage(Page):
    """An individual space that can be joined.

    Each instance of SpacePage represents a specific group or space available
    to students. It contains a description and an optional image to visually
    represent the space.
    """

    description = RichTextField()

    # A foreign key linking to Wagtail's built-in Image model.
    # This field is optional (null and blank allowed), and if the image is deleted,
    # the reference in the SpacePage is set to NULL (instead of deleting the page).
    # The related_name="+" disables the reverse relation from the image to this model.
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    # Defines the editing interface in the Wagtail admin.
    # It extends the default content panels provided by Page with panels
    # for editing the 'description' and 'image' fields.
    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("image"),
    ]
