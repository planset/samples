from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from app1 import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sample1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^snippets/$', 'app1.views.snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)$', 'app1.views.snippet_detail'),
)

