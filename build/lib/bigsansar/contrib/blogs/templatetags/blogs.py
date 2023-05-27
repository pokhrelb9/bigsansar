from django import template
from django.contrib.sites.shortcuts import get_current_site
from bigsansar.contrib.blogs.models import post
from bigsansar.contrib.sites.models import domains


register = template.Library()


@register.simple_tag(takes_context=True)
def get_blog(context):
    current_site = get_current_site(context['request'])
    get_pages_filter = post.objects.filter(domain__domain=current_site)

    return get_pages_filter


@register.simple_tag(takes_context=True)
def get_blog_object(context):
    get_path_args = context['request'].get_full_path().rsplit('/', 1)[1]
    dd = get_path_args.split('?')[0]
    current_site = get_current_site(context['request'])
    db = domains.objects.get(domain=current_site)
    get_blog_objects = post.objects.get(domain=db, slug=dd)

    return get_blog_objects