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
        context = super().get_context(request)

        from home.models import FollowingPage

        context["for_you_page"] = ForYouPage.objects.live().first()
        context["following_page"] = FollowingPage.objects.live().first()
        return context


class FollowingPage(Page):
    """A simple page that shows a placeholder for 'Following'."""

    content_panels = Page.content_panels
