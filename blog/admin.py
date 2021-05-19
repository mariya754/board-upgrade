from django.contrib import admin
from .models import Post, AdditionalImage, Comment


class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage

class CommentInline(admin.TabularInline):
    model =Comment

class BbAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title', 'body',)
    inlines = (AdditionalImageInline, CommentInline)


admin.site.register(Post, BbAdmin)
