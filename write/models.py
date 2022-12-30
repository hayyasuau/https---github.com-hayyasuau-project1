from django.db import models

# Create your models here.
class Join(models.Model):
    join_id = models.IntegerField(primary_key=True)
    comment = models.CharField(max_length=200)

class Free(models.Model):
    free_id = models.IntegerField(primary_key=True)
    text = models.TextField()
    comment = models.CharField(max_length=200)

class Gallery(models.Model):
    gallery_id = models.IntegerField(primary_key=True)
    comment = models.CharField(max_length=200)
    picture = models.CharField(max_length=200)


class Good(models.Model):
    good_id = models.AutoField(primary_key=True)
    free = models.ForeignKey(Free, on_delete=models.CASCADE,db_column='free_id', null=True)
    id = models.ForeignKey(Info, on_delete=models.CASCADE,db_column='info_id', null=True)
    join = models.ForeignKey(Join, on_delete=models.CASCADE,db_column='join_id', null=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE,db_column='gallery_id', null=True)