# Generated by Django 4.1.4 on 2023-01-07 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("make_moim", "0004_remove_category_make_moim_make_moim_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="make_moim",
            name="category",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name="Category",
        ),
    ]
