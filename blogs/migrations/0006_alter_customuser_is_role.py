# Generated by Django 4.1.1 on 2022-09-15 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_remove_customuser_is_bloger_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_role',
            field=models.CharField(choices=[('Reader', 'Reader'), ('bloger', 'Bloger')], default='---select---', max_length=10),
        ),
    ]
