# Generated by Django 3.0.2 on 2020-03-08 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200308_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='hero_subtitle_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_subtitle_ro',
            field=models.TextField(blank=True, null=True),
        ),
    ]
