from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Faq(models.Model):
    CATE_Faq = [
        ('1', '일반'),
        ('2', '계정'),
        ('3', '기타'),
    ]
    category = models.TextField(verbose_name = "카테고리", max_length=3, choices=CATE_Faq )
    title = models.CharField(verbose_name = "질의 제목", max_length=50)
    created_at = models.DateTimeField(verbose_name = "생성 일시", auto_now_add = True)
    updated_at = models.DateTimeField(verbose_name = "최종 수정 일시", auto_now = True)


class Inquiry(models.Model):
    CATE_Iaq = [
        ('1', '일반'),
        ('2', '계정'),
        ('3', '기타'),
    ]
    CATE_STATUS = [
        ('1', '문의 등록'),
        ('2', '접수 완료'),
        ('3', '답변 완료'),
    ]
    category = models.TextField(verbose_name = "카테고리", max_length=3, choices=CATE_Iaq )
    title = models.CharField(verbose_name = "질의 제목", max_length=50)
    email = models.CharField(verbose_name="이메일", max_length =30, blank = True)
    phone = models.CharField(verbose_name = "문자메세지", max_length =11, blank = True)
    is_email = models.BooleanField(verbose_name = "이메일 수신 여부", default = False)
    is_phone = models.BooleanField(verbose_name='문자메세지 수신 여부', default = False)
    content = models.TextField(verbose_name = "문의 내용")
    image = models.ImageField(verbose_name = '이미지', null = True, blank = True)
    created_at = models.DateTimeField(verbose_name = "생성 일시", auto_now_add = True)
    updated_at = models.DateTimeField(verbose_name = "최종 수정 일시", auto_now = True)
    status = models.TextField(verbose_name = "상태", max_length = 3, choices = CATE_STATUS)

    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name = 'inquiry_created_by')
    updated_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name = 'inquiry_updated_by')

class Answer(models.Model):
    content = models.TextField(verbose_name = "답변 내용")
    created_at = models.DateTimeField(verbose_name = "생성 일시", auto_now_add = True)
    updated_at = models.DateTimeField(verbose_name = "최종 수정 일시", auto_now = True)

    inquiry = models.ForeignKey(to="Inquiry", on_delete = models.CASCADE)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name = 'answer_created_by')
    updated_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name = 'answer_updated_by')