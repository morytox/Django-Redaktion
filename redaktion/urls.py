from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'redaktion.views.home', name='home'),
    # url(r'^redaktion/', include('redaktion.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^$', 'redaktion.main.views.home', {'template_name' :"home.html"}),
     url(r'^published/$', 'redaktion.main.views.published', {'template_name':"home.html"}),
     url(r'^archive/$', 'redaktion.main.views.archive', {'template_name' :"home.html"}),
     url(r'^draft/$', 'redaktion.main.views.draft', {'template_name' :"home.html"}),
     url(r'^profiles/', include('profiles.urls')),
     url(r'^accounts/', include('registration.backends.default.urls')),
)

