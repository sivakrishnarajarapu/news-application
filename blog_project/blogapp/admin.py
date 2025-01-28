from django.contrib import admin
from blogapp.models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','body','publish','created','updated','status']
    list_filter = ('status','author')   #It will display the side bar
    search_fields = ('title','body')    #Search the fields by these order
    raw_id_fields = ('author',)         #It will specify the author count
    date_hierarchy = 'publish'          #Date will display by publish date
    ordering = ('status','publish')     #display the ordering by these fields
    prepopulated_fields = {'slug':('title',)}   #it will says title as a slug

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','post','created','updated','active')
    list_filter = ('active','created','updated')
    search_fields = ('name','email','body')

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)

