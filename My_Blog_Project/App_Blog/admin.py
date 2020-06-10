from django.contrib import admin
from .models import Blog,Comment,Likes



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','author','blog_title','publish_date')
    list_filter = ('author','blog_title','publish_date')
    search_fields = ('blog_title','blog_content')
    date_hierarchy = 'publish_date'



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','blog','user','comment_date')
    list_filter = ('id','blog','user','comment_date')
    search_fields = ('id','blog','user','comment_date')
    date_hierarchy = 'comment_date'



@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('id','blog','user',)
    list_filter = ('id','blog','user',)
    search_fields = ('id','blog','user')
