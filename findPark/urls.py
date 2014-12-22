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

area_list = views.areaviewset.as_view({
    'get': 'list'
})

area_detail = views.areaviewset.as_view({
    'get': 'retrieve'
})

router = DefaultRouter()
router.register(r'parkingspots', views.parkingspotviewset)
router.register(r'areas', views.areaviewset)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'findPark.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^parkingspots/$', parkingspot_list, name='parkingspot-list'),
    url(r'^parkingspots/(?P<pk>[0-9]+)/$', parkingspot_detail, name='parkingspot-detail'),
    url(r'^areas/$', area_list, name='area-list'),
    url(r'^areas/(?P<pk>[0-9]+)/$', area_detail, name='area-detail')
)
