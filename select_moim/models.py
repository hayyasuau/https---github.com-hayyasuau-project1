from django.db import models

# Create your models here.
class Select_Moim(models.Model):#댓글 연결
    select_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    commend = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.content
