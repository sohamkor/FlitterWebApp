from django.contrib import admin

from .models import Fleeter, Post, Follower

# Register your models here.
admin.site.register(Fleeter)
admin.site.register(Post)
admin.site.register(Follower)
#admin.site.register(Following)
