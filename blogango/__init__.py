
from django.db.models import signals

from pingback.client import ping_external_links

from blogango.models import BlogEntry


def pingback_blog_handler(year, month, slug, **kwargs):
    return BlogEntry.objects.get(created_on__year=year,
                                 created_on__month=month,
                                 slug=slug,
                                 is_published=True)


# ping external links in the entry
def get_blog_text(instance):
    return instance.text.rendered

signals.post_save.connect(ping_external_links(content_func=get_blog_text,
                                              url_attr='get_absolute_url'),
                          sender=BlogEntry, weak=True)

default_app_config = 'blogango.apps.BlogangoConfig'
