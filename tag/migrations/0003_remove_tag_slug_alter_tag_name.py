# Generated by Django 4.1.4 on 2023-01-07 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tag", "0002_tagmoim"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tag",
            name="slug",
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
