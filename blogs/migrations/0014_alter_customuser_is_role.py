# Generated by Django 4.1.1 on 2022-09-19 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0013_alter_customuser_is_reader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_role',
            field=models.CharField(choices=[('Reader', 'Reader'), ('Bloger', 'Bloger')], default='', max_length=10, verbose_name='who are you?'),
        ),
    ]
