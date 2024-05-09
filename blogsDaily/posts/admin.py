from django.contrib import admin
from posts.models import Post
from posts.models import Category
from posts.models import Comment, Profile

#for configration of Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','descriptions','url','image')
    search_fields =('title','url')

class PostAdmin(admin.ModelAdmin):
    list_display=('title','subject','author', 'description', 'url','image')

# Register your models here.
admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(Profile)

