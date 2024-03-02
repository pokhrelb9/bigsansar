from django.contrib import admin
from bigsansar.contrib.blogs.forms import customblogform
from django.contrib.auth.models import User
from bigsansar.contrib.blogs.models import comment, post
from django.contrib.admin import SimpleListFilter
from django.utils.translation import gettext_lazy as _

from bigsansar.contrib.sites.models import domains



# Register your models here.
class domain_filter(SimpleListFilter):
    title = _('Domains')  # a label for our filter
    parameter_name = "domain"  # you can put anything here

    def lookups(self, request, model_admin):
        # This is where you create filter options; we have two:
        qs = model_admin.get_queryset(request)
        return qs.values_list('domain_id', 'domain__domain').order_by('domain').distinct()

    def queryset(self, request, queryset):

        # This is where you process parameters selected by use via filter options:
        if self.value():
            return queryset.filter(domain=self.value(), user=request.user)


class blogadmin(admin.ModelAdmin):
    form = customblogform
    list_display = ['title', 'publish_date', 'visitor']
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title']
    list_filter = (domain_filter,)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        qs = super().formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == "user":
            if request.user.is_superuser:
                return qs
            kwargs["queryset"] = User.objects.filter(username=request.user.username)

        elif db_field.name == "domain":
            if request.user.is_superuser:
                return qs
            get_domain = domains.objects.filter(user=request.user)
            kwargs["queryset"] = get_domain

        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class commentsadmin(admin.ModelAdmin):
    list_display = ['comments', 'user', 'publish_date']


admin.site.register(comment, commentsadmin)
admin.site.register(post, blogadmin)
