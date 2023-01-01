# Generated by Django 4.1.4 on 2022-12-30 12:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("write", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="free",
            name="hits",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="free",
            name="imgfile",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="free",
            name="title",
            field=models.CharField(default="", max_length=64, verbose_name="글 제목"),
        ),
        migrations.AddField(
            model_name="free",
            name="update_dttm",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="free",
            name="write_dttm",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="gallery",
            name="imgfile",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="free",
            name="text",
            field=models.TextField(verbose_name="글 내용"),
        ),
    ]