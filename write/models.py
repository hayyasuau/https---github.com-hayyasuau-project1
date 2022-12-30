from django.db import models

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
    good_id = models.IntegerField(primary_key=True)
