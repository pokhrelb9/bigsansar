from django import template
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from bigsansar.contrib.blogs.models import post
from bigsansar.contrib.sites.models import domains


register = template.Library()


@register.simple_tag(takes_context=True)
def get_blog(context):
    current_site = get_current_site(context['request'])
    get_pages_filter = post.objects.filter(domain__domain=current_site).order_by('-id')[:10]

    return get_pages_filter


@register.simple_tag(takes_context=True)
def get_blog_object(context):
    get_path_args = context['request'].get_full_path().rsplit('/', 1)[1]
    dd = get_path_args.split('?')[0]
    current_site = get_current_site(context['request'])
    try:
        db = domains.objects.get(domain=current_site)
        get_blog_objects = post.objects.get(domain=db, slug=dd)
        return get_blog_objects
       
    except:
         pass
    


@register.simple_tag(takes_context=True)
def update_blog_visitor(context):
    get_path_args = context['request'].get_full_path().rsplit('/', 1)[1]
    dd = get_path_args.split('?')[0]
    current_site = get_current_site(context['request'])
    try:
        db = domains.objects.get(domain=current_site)
        get_blog_objects = post.objects.get(domain=db, slug=dd)
        get_visitor = get_blog_objects.visitor + 1
        post.objects.filter(domain=db, slug=dd).update(visitor=get_visitor)

    except:
         pass
    
    return ''