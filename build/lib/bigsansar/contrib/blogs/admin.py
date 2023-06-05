from django.contrib import admin
from bigsansar.contrib.blogs.forms import customblogform

from bigsansar.contrib.blogs.models import comment, post


# Register your models here.


class blogadmin(admin.ModelAdmin):
    form = customblogform
    list_display = ['title', 'user', 'publish_date', 'visitor']
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title']
    list_filter = ('domain',)


class commentsadmin(admin.ModelAdmin):
    list_display = ['comments', 'user', 'publish_date']


admin.site.register(comment, commentsadmin)
admin.site.register(post, blogadmin)
