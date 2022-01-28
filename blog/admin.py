from django.contrib import admin
from .models import Author,Post,Tag,Comment

# Register your models here.
class Postadmin(admin.ModelAdmin):
    list_filter = ("author","tag","date")
    list_display = ("title","date","author")
    prepopulated_fields = {"slug":("title",)}

class Commentadmin(admin.ModelAdmin):
    list_filter = ("user_name")
    

admin.site.register(Author)
admin.site.register(Post,Postadmin)
admin.site.register(Tag)
admin.site.register(Comment)
