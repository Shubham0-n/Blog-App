# Generated by Django 4.0.4 on 2022-09-21 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0021_alter_comment_blog_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsdetails',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
