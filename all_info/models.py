from django.db import models

class Info(models.Model):
    id = models.CharField(max_length = 20)
    pw = models.CharField(max_length = 20)
    name = models.CharField(max_length = 20)
    region = models.CharField(max_length = 20)
    sex = models.CharField(max_length = 10)
    preference = models.CharField(max_length = 20)
    age = models.IntegerField(default=0)

class region(models.Model):
    region_id = models.IntegerField(default=0)
    region = models.CharField(max_length = 20)

class Group(models.Model):
    group_id = models.CharField(max_length = 20)
    group_name = models.CharField(max_length = 20)
    explain = models.TextField(default=0)

class Category(models.Model):
    category = models.IntegerField(default=0)
    category_name = models.CharField(max_length = 20)


class GroupInfo(models.Model):
    group_info_id = models.IntegerField(default=0)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    id = models.ForeignKey(Info, on_delete=models.CASCADE)
    y_n = models.CharField(max_length = 1)
    apply_date = models.CharField(max_length = 20)
    join_date = models.CharField(max_length = 20)