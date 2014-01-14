from django.db import models
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from datetime import datetime
from django import forms

import random

FILE_TYPE_CHOICES = (
    ('Image', 'Image'),
    ('Video', 'Video'),
    ('Youtube', 'Youtube'),

)

def unique_id():
    return random.randint(10000000,19999999)

class UserSearchForm(forms.Form):
    searchTerms = forms.CharField(max_length=255)

class Post(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    postId = models.IntegerField(default= lambda: random.randint(10000000,19999999))
    description = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=555)
    fileType = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES)
    published = models.BooleanField(default=False)
    dateSubmitted = models.DateTimeField(default= lambda: datetime.now())
    created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    unlikes = models.IntegerField(default=0)
    tags = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['-created']
        # unique_together = ("postId", "slug")
 
    def __unicode__(self):
        return u'%s' % self.title
 
    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])


class UserSubmittedPost(ModelForm):
    class Meta:
        model = Post
        postId = unique_id()
        slug = unique_id()
        exclude = ('published', 'likes', 'unlikes', 'created', 'slug', 'postId', 'dateSubmitted')