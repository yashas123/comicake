# Generated by Django 2.0.2 on 2018-03-12 01:56

from django.db import migrations, models
import reader.models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0009_auto_20180311_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='file',
            field=models.ImageField(upload_to=reader.models.Page.path),
        ),
        migrations.AlterField(
            model_name='page',
            name='height',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='mime',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='size',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='width',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
