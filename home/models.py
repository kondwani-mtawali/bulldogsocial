from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from foryou.models import ForYouPage  # import here to avoid circular imports


class HomePage(Page):
    """The main landing page for Bulldog Social."""

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    def get_context(self, request):
        """
        Override the default get_context() method to add extra context variables
        for use in the home page template.
        """
        # Call the superclass to get the default context dictionary.
        context = super().get_context(request)

        # Avoiding circular imports
        from home.models import FollowingPage

        # Gets first instance of for you page
        # Wagtail function.
        context["for_you_page"] = ForYouPage.objects.live().first()

        context["following_page"] = FollowingPage.objects.live().first()
        return context


class FollowingPage(Page):
    """Following Page content panels"""

    content_panels = Page.content_panels
