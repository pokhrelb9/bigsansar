from django import template

from bigsansar.contrib.advance.models import SidebarSettings
from bigsansar.contrib.sites.models import domains


register = template.Library()

@register.simple_tag(takes_context=True)
def get_is_sidebar_open(context):
    
    try:
        user = context['request'].user
        is_sidebar_open = SidebarSettings.objects.get(user=user)
        return is_sidebar_open
    
    except:
        return ''


@register.simple_tag(takes_context= True)
def post_is_sidebar_open(context):
    request = context['request']
    user = request.user
    if request.method == 'POST':
        if request.POST.get('nav_true') == 'True':

            check_default = request.POST.get('nav_true')
            SidebarSettings.objects.update_or_create(user=user, defaults={'is_sidebar_open': check_default})  # Fetch the settings object, you might want to filter properly
            return ''
        
        elif request.POST.get('nav_true') == 'False':
            check_default = request.POST.get('nav_true')
            SidebarSettings.objects.update_or_create(user=user, defaults={'is_sidebar_open': check_default})  # Fetch the settings object, you might want to filter properly
            return ''
        else:
            return ''
    else:
        return ''
    


@register.simple_tag(takes_context=True)
def host_for_nav(context):
    try:

        id = context['request'].META['PATH_INFO'].split("/")[4]
        ruser = context['request'].user
    except:
        return ''
    
    else:
        get_host = domains.objects.get(id=id, user=ruser)
        return get_host
    

@register.simple_tag(takes_context=True)
def domain_list_for_nav(context):
    user = context['request'].user
    domain = domains.objects.filter(user=user).order_by('-id')
    return domain