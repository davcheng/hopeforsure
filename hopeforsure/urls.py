from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
 
admin.autodiscover()
 
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', 'blog.views.about'),
    url(r'^top/', 'blog.views.top'),
    url(r'^(?P<slug>[\w\-]+)/upvote/$', 'blog.views.upvote'),
    #url(r'^(?P<slug>[\w\-]+)/id/$', 'blog.views.id'),
	url(r'^id/', 'blog.views.id'),
    url(r'^like/(?P<slug>[\w\-]+)/$', 'blog.views.like'),
	url(r'^testid/', 'blog.views.testid'),
    url(r'^$', 'blog.views.index'),
    url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),
)