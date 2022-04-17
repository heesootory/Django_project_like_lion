from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Faq(models.Model):
    QUESTION_CATE = (
        ('일반', '일반'),
        ('계정', '계정'),
        ('기타', '기타')
    )

    question = models.TextField(verbose_name ='질문', null = False, blank = True, default = "")
    category = models.CharField(verbose_name = '카테고리', max_length = 10, choices = QUESTION_CATE)
    answer = models.TextField(verbose_name = '답변',  null = True, blank = True)
    writer = models.ForeignKey(to = User, on_delete = models.CASCADE,  null = True, blank = True)
    create_date = models.DateTimeField(verbose_name = '생성일시', auto_now_add = True)
    final_modifier = models.CharField(verbose_name = '최종수정자', max_length = 10, default = User, null = True, blank = True)      #일대일 관계 매핑
    final_modify_date = models.DateTimeField(verbose_name = '최종 수정일시', auto_now = True)


