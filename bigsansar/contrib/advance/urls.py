from django.urls import include, path
from django.contrib import admin
from bigsansar.contrib.advance import views


urlpatterns = [
    path('', views.userlogin),
    path('account', views.account),
    path('logout', views.userlogout),
    path('bpanel', admin.site.urls),
    path('changeuname', views.chuname, name='changeuname'),
    path('changepass', views.chpass, name='changepass'),
    path("filelist/", include("ckeditor_uploader.urls")),
    path('account/edit', views.editprofile, name='editprofile'),
    path('domain/', include('bigsansar.contrib.sites.urls')),
    path('notify/update', views.admin_update_fun, name='admin update fun'),
    
]