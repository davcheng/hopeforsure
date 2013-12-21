from django.db import models
from django.core.urlresolvers import reverse
from django.forms import ModelForm
 
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    # tags = models.CharField(max_length=255)
    # unlike = models.CharField(max_length=255)
 
    class Meta:
        ordering = ['-created']
 
    def __unicode__(self):
        return u'%s' % self.title
 
    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])

