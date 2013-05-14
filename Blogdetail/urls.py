from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from MyBlog import settings
from Blogdetail.views import detail
#admin.autodiscover()

urlpatterns = patterns('',
    url(r'(\d{1,3})/$', 'Blogdetail.views.detail', name='detail'),
    )