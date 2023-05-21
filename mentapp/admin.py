from django.contrib import admin
from .models import *

# Register your models here.
class NewPostAdmin(admin.ModelAdmin):
    list_display=("title","date")


admin.site.register(NewPost, NewPostAdmin)
admin.site.register(Tag)
