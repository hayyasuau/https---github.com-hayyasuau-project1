from django.db import models


class Info(models.Model):
    info_id = models.CharField(max_length = 20, primary_key=True)
    pw = models.CharField(max_length = 20, null=True)
    name = models.CharField(max_length = 20)
    region = models.CharField(max_length = 20)
    sex = models.CharField(max_length = 10)
    preference = models.CharField(max_length = 20)
    age = models.IntegerField(default=0)

class Category(models.Model):
    category = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length = 20)
class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    region = models.CharField(max_length = 20, null=True)

class Group(models.Model):
    group_id = models.CharField(max_length = 20, primary_key=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,db_column='region_id', null=True)
    group_name = models.CharField(max_length = 20)
    explain = models.TextField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,db_column='category', null=True)



class GroupInfo(models.Model):
    group_info_id = models.AutoField(default=0, primary_key=True)
    info = models.ForeignKey(Info, on_delete=models.CASCADE,db_column='info_id', null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE,db_column='group_id', null=True)
    y_n = models.CharField(max_length = 1)
    apply_date = models.CharField(max_length = 20)
    join_date = models.CharField(max_length = 20)