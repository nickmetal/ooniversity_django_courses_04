# encoding: utf-8
from django.contrib import admin
from django.contrib.auth.models import User
from blog.models import Post, Tag


class PostAdmin(admin.ModelAdmin):

    """custom view for Post"""
    # list_display = ('name', 'short_description')
    search_fields =('title',)



admin.site.register(Post,  PostAdmin)
admin.site.register(Tag)
