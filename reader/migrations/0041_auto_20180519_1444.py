# Generated by Django 2.0.4 on 2018-05-19 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0040_auto_20180509_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic',
            name='format',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Comic'), (1, 'Manga'), (2, 'Toon')], default=1, help_text='Determines page layout in viewer'),
        ),
    ]
