from django.contrib import admin

# Register your models here.
from .models import blog,blog_comments


admin.site.register(blog)
admin.site.register(blog_comments)