# Generated by Django 4.1.1 on 2022-09-16 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0012_rename_is_user_customuser_is_reader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_reader',
            field=models.BooleanField(default=False, verbose_name='Reader'),
        ),
    ]
