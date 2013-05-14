from django.conf.urls import patterns, include, url
from MyBlog.views import list_all, details,welcome
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'MyBlog.views.welcome', name='home'),
    url(r'^myblogs$','MyBlog.views.list_all',name='listall'),
    url(r'^time/(\d{1,2})/$','MyBlog.views.details',name='details'),
    url(r'^blogs/',include('Blogdetail.urls')),
    # url(r'^MyBlog/', include('MyBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls))
)

urlpatterns += staticfiles_urlpatterns()

#This is the photo showing setting , you put the photo to the 'settings.MEDIA_ROOT' folder
urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_ROOT }),
    #(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    (r'^(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    ( r'^js/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_ROOT }), 
    ( r'^css/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT }), 
    #( r'^images/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT }), )
    #(r'^css/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root':settings.STATICFILES_DIRS}),
    )
