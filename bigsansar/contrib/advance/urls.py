from django.urls import include, path
from django.contrib import admin

from bigsansar.contrib.advance import views


urlpatterns = [
    path('', views.userlogin),
    path('dashboard', views.dashboard),
    path('logout', views.userlogout),
    path('bpanel', admin.site.urls),
    path('changeuname', views.chuname, name='changeuname'),
    path('changepass', views.chpass, name='changepass'),

    
]