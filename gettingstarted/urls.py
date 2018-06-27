from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import beerapp.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', beerapp.views.index, name='index'),
    path('admin/', admin.site.urls),
]
