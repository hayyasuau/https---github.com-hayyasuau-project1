from django.db import models
from all_info import models as models2
from django.conf import settings #좋아요-import setting
# Create your models here. 
class Join(models.Model):
    join_id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=200)
    info = models.ForeignKey(models2.Info, on_delete=models.CASCADE,db_column='info_id', null=True)
    group = models.ForeignKey(models2.Group, on_delete=models.CASCADE,db_column='group_id', null=True)
    new_face = models.TextField(verbose_name='가입인사')

    

class Free(models.Model):
    free_id = models.AutoField(primary_key=True)
    text = models.TextField(verbose_name='글 내용')
    comment = models.CharField(max_length=200)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles') #좋아요 추가
    info = models.ForeignKey(models2.Info, on_delete=models.CASCADE,db_column='info_id', null=True)
    group = models.ForeignKey(models2.Group, on_delete=models.CASCADE,db_column='group_id', null=True)
    title = models.CharField(max_length=64, verbose_name='글 제목', default='')
    write_dttm = models.DateTimeField(auto_now_add=True)
    update_dttm = models.DateTimeField(auto_now=True)
    hits=models.PositiveIntegerField(default=0)
    imgfile = models.ImageField(null=True, upload_to="", blank=True) # 이미지 컬럼 추가
    def __str__(self):
        return self.title
class Gallery(models.Model):
    gallery_id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=200)
    picture = models.CharField(max_length=200)
    info = models.ForeignKey(models2.Info, on_delete=models.CASCADE,db_column='info_id', null=True)
    group = models.ForeignKey(models2.Group, on_delete=models.CASCADE,db_column='group_id', null=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True) # 이미지 컬럼 추가


class Good(models.Model):#댓글 연결
    good_id = models.AutoField(primary_key=True)
    free = models.ForeignKey(Free, on_delete=models.CASCADE,db_column='free_id', null=True)
    info = models.ForeignKey(models2.Info, on_delete=models.CASCADE,db_column='info_id', null=True)
    join = models.ForeignKey(Join, on_delete=models.CASCADE,db_column='join_id', null=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE,db_column='gallery_id', null=True)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content

