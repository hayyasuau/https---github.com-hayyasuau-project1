# Generated by Django 4.1 on 2023-01-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("write", "0004_remove_free_make_moim_remove_free_select_moim"),
    ]

    operations = [
        migrations.AddField(
            model_name="good",
            name="title",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
