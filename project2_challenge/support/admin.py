from django.contrib import admin
from .models import Inquiry, Answer

# Register your models here.

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('category', 'subject' ,'email', 'email_receive', 'message', 'message_receive', 'content', 'image')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('content','reference','create_date','final_modify_date','final_modifier','writer','inquiry')

