from django.db import models
from all_info import models as models2 
# Create your models here.
class Join(models.Model):
    join_id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=200)
    info = models.ForeignKey(models2.Info, on_delete=models.CASCADE,db_column='info_id', null=True)
    group = models.ForeignKey(models2.Group, on_delete=models.CASCADE,db_column='group_id', null=True)

    

class Free(models.Model):
    free_id = models.AutoField(primary_key=True)
    text = models.TextField(verbose_name='글 내용')
    comment = models.CharField(max_length=200)    
    info = models.ForeignKey(models2.Info, on_delete=models.CASCADE,db_column='info_id', null=True)
    group = models.ForeignKey(models2.Group, on_delete=models.CASCADE,db_column='group_id', null=True)
    title = models.CharField(max_length=64, verbose_name='글 제목')
    write_dttm = models.DateTimeField(auto_now_add=True)
    update_dttm = models.DateTimeField(auto_now=True)
    hits=models.PositiveIntegerField(default=0)

class Gallery(models.Model):
    gallery_id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=200)
    picture = models.CharField(max_length=200)
    info = models.ForeignKey(models2.Info, on_delete=models.CASCADE,db_column='info_id', null=True)
    group = models.ForeignKey(models2.Group, on_delete=models.CASCADE,db_column='group_id', null=True)


class Good(models.Model):
    good_id = models.AutoField(primary_key=True)
    free = models.ForeignKey(Free, on_delete=models.CASCADE,db_column='free_id', null=True)
    info = models.ForeignKey(models2.Info, on_delete=models.CASCADE,db_column='info_id', null=True)
    join = models.ForeignKey(Join, on_delete=models.CASCADE,db_column='join_id', null=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE,db_column='gallery_id', null=True)