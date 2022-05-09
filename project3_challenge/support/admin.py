from django.contrib import admin
from .models import Faq, Inquiry, Answer
# Register your models here.


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


@admin.action(description="답변 완료 문자/이메일 전송!")
def make_published(modeladmin, request, queryset):
    for q in queryset:
        if q.is_phone == True:
            print(f'{q.created_by}님의 전화번호- {q.phone}으로 문자 발송완료.')
        if q.is_email == True:
            print(f'{q.created_by}님의 메일 - {q.email}로 메일 발송완료.')


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'updated_at')
    list_filter = ('category',)
    search_fields = ('title',)
    search_help_text = "제목을 검색하세요."


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'created_by', 'status')
    list_filter = ('category', 'status')
    search_fields = ('title', 'phone', 'email', 'created_by__username')
    readonly_field = ('created_at',)
    search_help_text = "제목/이메일/폰넘버 검색이 가능합니다."
    inlines = [AnswerInline]

    actions = [make_published]
