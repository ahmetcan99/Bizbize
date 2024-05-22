from django.contrib import admin
from .models import Post, UserProfile, Comment, Reply
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(UserProfile)
