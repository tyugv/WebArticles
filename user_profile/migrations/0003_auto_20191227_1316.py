# Generated by Django 3.0 on 2019-12-27 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20191227_1316'),
        ('user_profile', '0002_user_profile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='articles',
            field=models.ManyToManyField(blank=True, to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]