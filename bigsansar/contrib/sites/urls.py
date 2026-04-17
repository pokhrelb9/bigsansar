from django.urls import path

from bigsansar.contrib.sites import views



urlpatterns = [
    path('manage/<id>', views.manage_domain, name='manage doamin'),
    path('create', views.create_domain, name='create domain'),
    path('manage/<id>/edit', views.edit_host, name='edit domain'),
    path('manage/<id>/pages/create', views.page_create, name='pages add'),
    path('manage/<id>/pages/<pagesid>/edit', views.pages_edit, name='pages edit panel'),
    path('manage/<id>/pages/<pagesid>/delete', views.page_delete, name='page delete'),
    
 ]