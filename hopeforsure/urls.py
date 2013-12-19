from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
 
admin.autodiscover()
 
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', 'blog.views.about'),
    url(r'^top/', 'blog.views.top'),
    url(r'^next/(?P<current_page>\d+)/$', 'blog.views.nextfiveposts'),
    url(r'^back/(?P<current_page>\d+)/$', 'blog.views.backfiveposts'),
    url(r'^like/(?P<slug>[\w\-]+)/$', 'blog.views.like'),
    url(r'^$', 'blog.views.index'),
    url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),
)