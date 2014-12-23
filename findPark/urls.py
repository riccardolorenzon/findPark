from django.conf.urls import patterns, include, url
from django.contrib import admin
import findParkBackend.views as views
from rest_framework.routers import DefaultRouter
from rest_framework import renderers

#parkingspot
parkingspot_list = views.parkingspotviewset.as_view({
    'get': 'list',
    'post': 'create'
})
parkingspot_detail = views.parkingspotviewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

parkingarea_list = views.parkingareaviewset.as_view({
    'get': 'list',
    'post': 'create'
})

parkingarea_detail = views.parkingareaviewset.as_view({
    'get': 'retrieve'
})

router = DefaultRouter()
router.register(r'parkingspots', views.parkingspotviewset)
router.register(r'parkingareas', views.parkingareaviewset)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'findPark.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/parkingspots/$', parkingspot_list, name='parkingspot-list'),
    url(r'^api/parkingspots/(?P<pk>[0-9]+)/$', parkingspot_detail, name='parkingspot-detail'),
    url(r'^api/parkingareas/$', parkingarea_list, name='parkingarea-list'),
    url(r'^api/parkingareas/(?P<pk>[0-9]+)/$', parkingarea_detail, name='parkingarea-detail')
)
