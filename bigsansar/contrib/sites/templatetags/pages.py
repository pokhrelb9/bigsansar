from django import template
from django.contrib.sites.shortcuts import get_current_site
from bigsansar.contrib.sites.models import pages


register = template.Library()


@register.simple_tag(takes_context=True)
def get_pages(context):
    current_site = get_current_site(context['request'])
    get_pages_filter = pages.objects.filter(domain__domain=current_site)

    return get_pages_filter
