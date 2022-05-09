from django.contrib import admin
from .models import Faq, Inquiry, Answer
# Register your models here.


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'updated_at')
    list_filter = ('category',)
    search_fields = ('title',)
    search_help_text = "제목을 검색하세요."

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'created_by')
    list_filter = ('category',)
    search_fields = ('title', 'email', 'phone')
    readonly_field  = ('created_at',)
    search_help_text = "제목/이메일/폰넘버 검색이 가능합니다."
    inlines = [AnswerInline]

    