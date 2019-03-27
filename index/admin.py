from django.contrib import admin
from .models import *



#定义高级管理类
class AuthorAdmin(admin.ModelAdmin):
    #定义在列表页上允许显示的字段
    list_display = ['name','age','email']
    #定义在列表页中能连接到详情页的字段
    list_display_links = ['name','email']
    #定义在列表页中就允许修改的字段们
    list_editable = ['age']
    #定义允许被搜索的字段
    search_fields = ['name','email']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','publicate_date']
    #定义时间分层
    # date_hierarchy = 'publicate_date'

# Register your models here.
admin.site.register(Author,AuthorAdmin)
admin.site.register(Publisher)
admin.site.register(Book,BookAdmin)
admin.site.register(Wife)
