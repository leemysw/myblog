from django.contrib import admin
from blog.models import Blog, Category, Tag, View


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'click_nums', 'category', 'create_time', 'modify_time']
    search_fields = ('title', 'create_time', 'category', 'tag')

class ViewAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['ip', 'ip_count', 'ip_address', 'view_time']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(View, ViewAdmin)
