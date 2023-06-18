from django.contrib import admin
from bigsansar.contrib.advance.models import javascript
# Register your models here.


class adminjava(admin.ModelAdmin):
    pass

admin.site.register(javascript, adminjava)
