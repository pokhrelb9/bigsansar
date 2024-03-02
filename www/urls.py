from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
path("filelist/", include("ckeditor_uploader.urls")),
path("", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = "BIGSANSAR"
admin.site.site_title = "Bigsansar"
admin.site.index_title = "bigsansar - create your own sites"
