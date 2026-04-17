from django.urls import path
from bigsansar.contrib.advance import views


urlpatterns = [
    path('', views.cloudflare),
    path('api_key', views.cf_conf, name='cloudflare api configrations'),
    path('hostname', views.cf_main_domain, name = 'main server domain'),
    path('ssl_origin', views.ssl_origin, name='ssl_origin'),
    # path('a', views.ff)
]