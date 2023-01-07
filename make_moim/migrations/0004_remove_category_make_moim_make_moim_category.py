# Generated by Django 4.1.4 on 2023-01-07 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("make_moim", "0003_remove_make_moim_tags_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="make_moim",
        ),
        migrations.AddField(
            model_name="make_moim",
            name="category",
            field=models.ForeignKey(
                db_column="category",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="make_moim.category",
            ),
        ),
    ]
