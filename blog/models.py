from wagtail.models import Page
from wagtail.fields import RichTextField
from django.db import models
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from modelcluster.fields import ParentalKey
from django.shortcuts import render
from .forms import ContactForm

class BlogIndexPage(Page):
    template = 'blog/index.html'
    subpage_types = ['blog.BlogPage']

    def get_context(self, request):
        context = super().get_context(request)
        context['posts'] = BlogPage.objects.live().descendant_of(self).order_by('-first_published_at')
        return context

class BlogPage(Page):
    template = 'blog/post.html'
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField()
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('header_image'),
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

class ContactPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    def serve(self, request):
        form = ContactForm(request.POST or None)
        form_submitted = False

        if request.method == "POST" and form.is_valid():
            ContactSubmission.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message']
            )
            form_submitted = True
            form = ContactForm()  # reset form after submission

        return render(request, "blog/contact.html", {
            "page": self,
            "form": form,
            "form_submitted": form_submitted
        })

class FormField(AbstractFormField):
    page = ParentalKey('ContactFormPage', related_name='form_fields')

class ContactFormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldPanel('to_address'),
            FieldPanel('from_address'),
            FieldPanel('subject'),
        ], heading="Email settings"),
    ]

class ContactSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

class AboutPage(Page):
    template = 'blog/about.html'
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
    ]

class PrivacyPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Privacy Policy Page"
