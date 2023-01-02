# Generated by Django 4.1 on 2023-01-02 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("select_moim", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("all_info", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Free",
            fields=[
                ("free_id", models.AutoField(primary_key=True, serialize=False)),
                ("text", models.TextField(null=True, verbose_name="글 내용")),
                ("comment", models.CharField(max_length=200, null=True)),
                (
                    "title",
                    models.CharField(default="", max_length=64, verbose_name="글 제목"),
                ),
                ("write_dttm", models.DateTimeField(auto_now_add=True, null=True)),
                ("update_dttm", models.DateTimeField(auto_now=True, null=True)),
                ("hits", models.PositiveIntegerField(default=0)),
                ("imgfile", models.ImageField(blank=True, null=True, upload_to="")),
                (
                    "group",
                    models.ForeignKey(
                        db_column="group_id",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="all_info.group",
                    ),
                ),
                (
                    "info",
                    models.ForeignKey(
                        db_column="info_id",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="all_info.info",
                    ),
                ),
                (
                    "like_users",
                    models.ManyToManyField(
                        related_name="like_articles", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "select_moim",
                    models.ForeignKey(
                        db_column="select_id",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="select_moim.select_moim",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Gallery",
            fields=[
                ("gallery_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "title",
                    models.CharField(default="", max_length=64, verbose_name="글 제목"),
                ),
                ("comment", models.CharField(max_length=200, null=True)),
                ("picture", models.CharField(max_length=200, null=True)),
                ("write_dttm", models.DateTimeField(auto_now_add=True, null=True)),
                ("update_dttm", models.DateTimeField(auto_now=True, null=True)),
                ("imgfile", models.ImageField(blank=True, null=True, upload_to="")),
                (
                    "group",
                    models.ForeignKey(
                        db_column="group_id",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="all_info.group",
                    ),
                ),
                (
                    "info",
                    models.ForeignKey(
                        db_column="info_id",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="all_info.info",
                    ),
                ),
                (
                    "select_moim",
                    models.ForeignKey(
                        db_column="select_id",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="select_moim.select_moim",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Join",
            fields=[
                ("join_id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=200, null=True)),
                ("comment", models.CharField(max_length=200, null=True)),
                ("write_dttm", models.DateTimeField(auto_now_add=True, null=True)),
                ("update_dttm", models.DateTimeField(auto_now=True, null=True)),
                ("new_face", models.TextField(null=True, verbose_name="가입인사")),
                (
                    "group",
                    models.ForeignKey(
                        db_column="group_id",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="all_info.group",
                    ),
                ),
                (
                    "info",
                    models.ForeignKey(
                        db_column="info_id",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="all_info.info",
                    ),
                ),
                (
                    "select_moim",
                    models.ForeignKey(
                        db_column="select_id",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="select_moim.select_moim",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Good",
            fields=[
                ("good_id", models.AutoField(primary_key=True, serialize=False)),
                ("content", models.CharField(max_length=200, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "free",
                    models.ForeignKey(
                        db_column="free_id",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="write.free",
                    ),
                ),
                (
                    "gallery",
                    models.ForeignKey(
                        db_column="gallery_id",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="write.gallery",
                    ),
                ),
                (
                    "info",
                    models.ForeignKey(
                        db_column="info_id",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="all_info.info",
                    ),
                ),
                (
                    "join",
                    models.ForeignKey(
                        db_column="join_id",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="write.join",
                    ),
                ),
                (
                    "select_moim",
                    models.ForeignKey(
                        db_column="select_id",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="select_moim.select_moim",
                    ),
                ),
            ],
        ),
    ]
