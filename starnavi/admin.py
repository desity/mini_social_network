from django.contrib import admin

# Register your models here.
from .models import Post, Like_Unlike


#admin.site.register(User)
admin.site.register(Post)
admin.site.register(Like_Unlike)