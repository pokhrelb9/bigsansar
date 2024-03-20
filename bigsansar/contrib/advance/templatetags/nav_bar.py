from django import template

from bigsansar.contrib.advance.models import SidebarSettings


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