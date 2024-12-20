# Generated by Django 5.1.4 on 2024-12-09 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_author_post_slug_alter_post_content_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                allow_unicode=True, blank=True, null=True, unique=True
            ),
        ),
    ]
