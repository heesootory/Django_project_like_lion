from django.contrib import admin

# Register your models here.
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    verbose_name = '댓글'
    extra = 1


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'content',
                    'created_at', 'view_count', 'writer')
    list_filter = ('created_at', )
    search_fields = ('id', 'writer',)
    search_help_text = '작성자, 게시판 번호로 검색'
    inlines = [CommentInline]

    actions = ['make_published']


def make_published(modeladmin, request, queryset):
    for item in queryset:
        item.content = "메롱"
        item.save()
