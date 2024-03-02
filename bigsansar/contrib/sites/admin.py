from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.utils.translation import gettext_lazy as _
from bigsansar.contrib.sites.forms import create_domainform, customaddpageform, custompageform
from bigsansar.contrib.sites.models import default_domain, domains, pages
from django.contrib.auth.models import User


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
            return queryset.filter(domain=self.value())




class pageadmin(admin.ModelAdmin):
    add_form = customaddpageform
    form = custompageform
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['slug', 'domain', 'publish_date', 'visitor']
    list_filter = (domain_filter,)
    search_fields = ['slug']

    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during foo creation
        """
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)
        


admin.site.register(pages, pageadmin)
