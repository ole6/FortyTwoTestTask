from django.conf.urls import patterns, include, url
from apps.hello.views import home

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^$', home, name='home'),

    url(r'^admin/', include(admin.site.urls)),
)
