# Generated by Django 4.1.1 on 2022-09-14 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='published',
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
