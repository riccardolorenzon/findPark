from django.conf.urls import patterns, include, url
from django.contrib import admin
import findParkBackend.views as views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'findPark.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.index),

)
