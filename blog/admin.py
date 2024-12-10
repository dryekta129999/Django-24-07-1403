from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author','created_date','updated_date','status')
	list_filter = ('status','created_date','updated_date')
	ordering = ('-created_date',)






admin.site.register(Post, PostAdmin)