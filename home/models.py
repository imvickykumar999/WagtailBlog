from wagtail.models import Page

class HomePage(Page):
    subpage_types = [
        'blog.ContactPage', 
        'blog.BlogIndexPage', 
        'blog.BlogPage',
        'blog.AboutPage',
        'blog.PrivacyPage',
        'home.HomePage',
    ]
