from django.contrib import admin
from bigsansar.contrib.advance.models import css, javascript
# Register your models here.

class admincss(admin.ModelAdmin):
    pass
class adminjava(admin.ModelAdmin):
    pass

admin.site.register(javascript, adminjava)
admin.site.register(css,admincss)


