from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from bigsansar.contrib.account.models import userinfo


# Register your models here.


class AccountInline(admin.StackedInline):
    model = userinfo
    can_delete = False
    verbose_name_plural = 'Accounts info'


class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInline, )


admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
