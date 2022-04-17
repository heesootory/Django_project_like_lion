from django.db import models
from django.contrib.auth import get_user_model 

# Create your models here.

User = get_user_model()

class Inquiry(models.Model):
    cate = (
        ('환불', '환불'),
        ('반품', '반품'),
        ('사이즈 교환', '사이즈 교환'),
        ('배송지 변경', '배송지 변경'),
    )
    category = models.CharField(verbose_name = '카테고리', max_length = 10, choices = cate)
    subject = models.CharField(verbose_name = '제목', max_length = 50)
    email = models.EmailField(verbose_name = '이메일', max_length = 254, null = True, blank = True)
    email_receive = models.BooleanField(default = False)
    message = models.CharField(verbose_name = '문자', max_length = 500, null = True, blank = True)
    message_receive = models.BooleanField(default = False)
    content = models.TextField(verbose_name = '내용')
    image = models.ImageField(verbose_name = '이미지', null = True, blank = True)


class Answer(models.Model):
    content = models.TextField(verbose_name = '내용')
    reference = models.URLField('site_url', null = True, blank = True)
    create_date = models.DateTimeField(verbose_name = '작성일', auto_now_add = True)
    final_modify_date = models.DateTimeField(verbose_name = '수정일', auto_now = True) 
    final_modifier = models.CharField(verbose_name = '최종수정자', max_length =20, null = True, blank = True)
    writer = models.ForeignKey(to = User, on_delete = models.CASCADE)
    inquiry = models.ForeignKey(to = 'Inquiry', on_delete = models.CASCADE)




