from django.contrib import admin

from .models import Post, PostImage, PostTag


class PostImageInline(admin.StackedInline):
    model = PostImage


class PostTagInline(admin.StackedInline):
    model = PostTag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline, PostTagInline]

    class Meta:
        model = Post


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    pass