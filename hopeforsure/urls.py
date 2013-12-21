from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
 
admin.autodiscover()
 
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', 'blog.views.about'),
    url(r'^top/', 'blog.views.top'),
    url(r'^random/', 'blog.views.random'),
    url(r'^next/top/(?P<current_page>\d+)/$', 'blog.views.nextfivetopposts'),
    url(r'^back/top/(?P<current_page>\d+)/$', 'blog.views.backfivetopposts'),    
    url(r'^next/(?P<current_page>\d+)/$', 'blog.views.nextfiveposts'),
    url(r'^back/(?P<current_page>\d+)/$', 'blog.views.backfiveposts'),
    url(r'^like/(?P<slug>[\w\-]+)/$', 'blog.views.like'),
    url(r'^$', 'blog.views.index'),
    url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),
    # url(r'^(?P<slug>[\w\-]+)#disqus_thread/$', 'blog.views.post'),
)