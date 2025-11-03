from django.db import models
from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from . import blocks as home_blocks


class HomePage(Page):
    content = StreamField([
        ('hero_banner', home_blocks.HeroBannerBlock()),
        ('mission_vision', home_blocks.MissionVisionBlock()),
        ('impact_stats', home_blocks.ImpactStatsBlock()),
        ('featured_programs', home_blocks.FeaturedProgramsBlock()),
        ('testimonial_carousel', home_blocks.TestimonialCarouselBlock()),
        ('news_updates', home_blocks.NewsUpdatesBlock()),
        ('call_to_action', home_blocks.CallToActionBlock()),
        ('partner_logos', home_blocks.PartnerLogosBlock()),
        ('contact_form', home_blocks.ContactFormBlock()),
        ('video_highlight', home_blocks.VideoHighlightBlock()),
        ('donation_progress', home_blocks.DonationProgressBlock()),
        ('map_location', home_blocks.MapLocationBlock()),
        ('spacer', home_blocks.SpacerBlock()),
        ('divider', home_blocks.DividerBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]


class ArticlePage(Page):
    date = models.DateField("Published date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    featured_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("body"),
        FieldPanel("featured_image"),
    ]

    parent_page_types = ["home.HomePage"]
    subpage_types = []


class ProgramPage(Page):
    description = RichTextField(blank=True)
    featured_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    contact_link = models.URLField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("featured_image"),
        FieldPanel("contact_link"),
    ]

    parent_page_types = ["home.HomePage"]
    subpage_types = []


@register_snippet
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    quote = models.TextField()
    photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("quote"),
        FieldPanel("photo"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"


@register_snippet
class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    website = models.URLField(blank=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("logo"),
        FieldPanel("website"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Partner Organization"
        verbose_name_plural = "Partner Organizations"
