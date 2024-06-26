# Generated by Django 5.0.4 on 2024-04-18 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comment_text_comment_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
