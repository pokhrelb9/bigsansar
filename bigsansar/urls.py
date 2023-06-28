"""www URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from bigsansar.contrib.advance import urls , views as v
from bigsansar import views


urlpatterns = [
    path('admin', v.admin_redirect, name='admin redirect'),
    path('admin/', include(urls)),
    path('sitemap.xml', views.sitemap, name= 'sitemap'),
    path('script.js', views.getjavascript, name = 'javascripts'),
    path('styles.css', views.getcss, name = 'custom css'),
    path('', views.index, name='index'),
    path('<url>', views.pathviews, name='path'),
    path('<path>/<slug>', views.get_path_url, name = 'get_path_args'),

]
