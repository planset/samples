from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('debugsample.myapp.views',
    # Examples:
    # url(r'^$', 'debugsample.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'index'),
)

