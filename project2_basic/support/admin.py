from django.contrib import admin

from .models import Faq

# Register your models here.
@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('id','question', 'category', 'answer', 'create_date', 'writer','final_modifier', 'final_modify_date')




