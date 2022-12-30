from django.db import models

# Create your models here.
class Good(models.Model):
    good_id = models.AutoField(primary_key=True)
    free = models.ForeignKey(Free, on_delete=models.CASCADE,db_column='free_id', null=True)
    id = models.ForeignKey(Info, on_delete=models.CASCADE,db_column='info_id', null=True)
    join = models.ForeignKey(Join, on_delete=models.CASCADE,db_column='join_id', null=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE,db_column='gallery_id', null=True)
