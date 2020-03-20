from django.contrib import admin
from .models import User, Post, Relationships

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Username',              {'fields': ['username']}),
        ('Password',              {'fields': ['password']}),
        ('FirstName',             {'fields': ['firstName']}),
        ('LastName',              {'fields': ['lastName']}),
        ('relationships',         {'fields': ['relationships']})
    ]
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Username',              {'fields': ['username']}),
        ('Body Text',             {'fields': ['bodyText']}),
        ('Date Created',          {'fields': ['dateCreated']}),
        ('Likes',                 {'fields': ['likes']}),
        ('User Id',               {'fields': ['userId']}),
    ]

class Relationships(admin.ModelAdmin):
    fieldsets = [
        ('Followers',             {'fields': ['followers']}),
        ('Following',             {'fields': ['following']}),
    ]

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Relationships)
