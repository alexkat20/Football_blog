# Generated by Django 3.1.4 on 2020-12-28 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_parser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Title '),
        ),
    ]