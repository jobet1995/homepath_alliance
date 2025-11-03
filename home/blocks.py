from wagtail import blocks
from wagtail.blocks import (
    CharBlock, TextBlock, RichTextBlock, ListBlock, PageChooserBlock, 
    URLBlock, ChoiceBlock, IntegerBlock, StructBlock
)
from wagtail.images.blocks import ImageChooserBlock

class HeroBannerBlock(blocks.StructBlock):
    title = CharBlock(required=True, help_text="Title of the hero banner")
    subtitle = TextBlock(required=False, help_text="Subtitle of the hero banner")
    image = ImageChooserBlock(required=True, help_text="Image of the hero banner")
    cta_button = CharBlock(required=False, help_text="Call to action button text")
    cta_button_url = URLBlock(required=False, help_text="Call to action button URL")

    class Meta:
        icon = "image"
        label = "Hero Banner"
        template = "home/blocks/hero_banner_block.html"

class MissionVisionBlock(blocks.StructBlock):
    mission_title = CharBlock(required=True, help_text="Title of the mission section")
    mission_content = RichTextBlock(required=True, help_text="Content of the mission section")
    vision_title = CharBlock(required=True, help_text="Title of the vision section")
    vision_content = RichTextBlock(required=True, help_text="Content of the vision section")
    illustration = ImageChooserBlock(required=True, help_text="Illustration of the mission and vision section")

    class Meta:
        icon = "group"
        label = "Mission & Vision"
        template = "home/blocks/mission_vision_block.html"

class ImpactStatsBlock(blocks.StructBlock):
    title = CharBlock(required=True, help_text="Title of the impact stats section")
    stats = ListBlock(
        StructBlock([
            ("label", CharBlock()),
            ("value", IntegerBlock())
        ])
    )
    background_style = ChoiceBlock(
        choices=[("light", "Light"), ("dark", "Dark"), ("themed", "Themed")],
        default="light"
    )
    
    class Meta:
        icon = "success"
        label = "Impact Stats"
        template = "home/blocks/impact_stats_block.html"

class FeaturedProgramsBlock(blocks.StructBlock):
    section_title = CharBlock(required=True, help_text="Title of the feature programs section")
    programs = ListBlock(
        StructBlock([
            ("program_image", ImageChooserBlock()),
            ("program_title", CharBlock()),
            ("program_description", TextBlock()),
            ("program_link", PageChooserBlock(required=False))
        ])
    )

    class Meta:
        icon = "folder-open-inverse"
        label = "Feature Programs"
        template = "home/blocks/feature_programs_block.html"

class TestimonialCarouselBlock(blocks.StructBlock):
    section_title = CharBlock(required=True)
    testimonials = ListBlock(
        StructBlock([
            ("name", CharBlock()),
            ("quote", TextBlock()),
            ("photo", ImageChooserBlock(required=False))
        ])
    )

    class Meta:
        icon = "user"
        label = "Testimonial Carousel"
        template = "home/blocks/testimonial_carousel_block.html"

class NewsUpdatesBlock(blocks.StructBlock):
    section_title = CharBlock(required=True)
    number_of_articles = IntegerBlock(default=3)

    class Meta:
        icon = "doc-full"
        label = "News Updates"
        template = "home/blocks/news_updates_block.html"

class CallToActionBlock(blocks.StructBlock):
    heading = CharBlock(required=True)
    text = TextBlock(required=True)
    button_text = CharBlock(required=True)
    button_link = PageChooserBlock(required=True)
    background_image = ImageChooserBlock(required=False)

    class Meta:
        icon = "edit"
        label = "Call to Action"
        template = "home/blocks/call_to_action_block.html"


class PartnerLogosBlock(blocks.StructBlock):
    title = CharBlock(required=True)
    logos = ListBlock(ImageChooserBlock())

    class Meta:
        icon = "group"
        label = "Partner Logos"
        template = "home/blocks/partner_logos_block.html"

class ContactFormBlock(blocks.StructBlock):
    title = CharBlock(required=True)
    intro_text = TextBlock(required=False)

    class Meta:
        icon = "mail"
        label = "Contact Form"
        template = "home/blocks/contact_form_block.html"

class VideoHighlightBlock(blocks.StructBlock):
    title = CharBlock(required=True)
    video_url = URLBlock(required=True)
    caption = TextBlock(required=False)

    class Meta:
        icon = "media"
        label = "Video Highlight"
        template = "home/blocks/video_highlight_block.html"

class DonationProgressBlock(blocks.StructBlock):
    title = CharBlock(required=True)
    goal_amount = IntegerBlock(required=True)
    current_amount = IntegerBlock(required=True)

    class Meta:
        icon = "pick"
        label = "Donation Progress"
        template = "home/blocks/donation_progress_block.html"

class MapLocationBlock(blocks.StructBlock):
    title = CharBlock(required=True)
    map_embed_url = URLBlock(required=True)

    class Meta:
        icon = "site"
        label = "Map Location"
        template = "home/blocks/map_location_block.html"


class SpacerBlock(blocks.StructBlock):
    height = ChoiceBlock(
        choices=[
            ("small", "Small"),
            ("medium", "Medium"),
            ("large", "Large"),
        ],
        default="medium"
    )

    class Meta:
        icon = "fa-arrow-down"
        label = "Spacer"
        template = "home/blocks/spacer_block.html"

class DividerBlock(blocks.StructBlock):
    class Meta:
        icon="horizontal-rule"
        label="Divider"
        template="home/blocks/divider_block.html"
