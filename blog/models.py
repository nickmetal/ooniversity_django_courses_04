# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    """docstring for TagsModel
       name
    """
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return '%s' % self.name

    def __str__(self):
        return '%s' % self.name


class Post(models.Model):
    """docstring for PostModel
       title, post_content, date, author, tags
    """
    title = models.CharField(max_length=100)
    post_content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True,
                                blank=True,null=True)
    # public_date = models.DateTimeField(blank=True)

    author = models.ForeignKey(User, verbose_name=('author'))
    tags = models.ManyToManyField(Tag, blank=True)
    # date = models.SlugField(max_length=200)


    def __unicode__(self):
        return '%s' % self.title

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return '/blog/%s/' % self.title



