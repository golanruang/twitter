from django.contrib import admin
from .models import User, Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['userName']}),
        (None,              {'fields': ['bodyText']}),
        (None,              {'fields': ['dateCreated']}),
        (None,              {'fields': ['likes']}),
        (None,              {'fields': ['userId']}),
        (None,              {'fields': ['likedBy']}),
    ]

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['username']}),
        (None,              {'fields': ['firstName']}),
        (None,              {'fields': ['lastName']}),
        (None,              {'fields': ['password']}),
        (None,              {'fields': ['followers']}),
        (None,              {'fields': ['following']}),
    ]

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
