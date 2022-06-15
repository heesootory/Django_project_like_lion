from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Post(models.Model):           #1대다 관계, post - "다"이므로, "1"인 writer를 foreignkey로 지정해줌
    image = models.ImageField(verbose_name = '이미지', null = True, blank = True)
    content = models.TextField(verbose_name = '내용')
    created_at = models.DateTimeField(verbose_name = '작성일', auto_now_add = True)
    view_count = models.IntegerField(verbose_name = '조회수', default = 0)
    writer = models.ForeignKey(to = User, on_delete = models.CASCADE, null = True, blank = True)

class Comment(models.Model):        #1대다 관계, comment - "다"이므로, "1"인 writer를 foreignkey로 지정해줌
    content = models.TextField(verbose_name = '내용')
    created_at = models.DateTimeField(verbose_name = '작성일')
    post = models.ForeignKey(to="Post", on_delete = models.CASCADE)
    writers =  models.ForeignKey(to = User, on_delete = models.CASCADE)


