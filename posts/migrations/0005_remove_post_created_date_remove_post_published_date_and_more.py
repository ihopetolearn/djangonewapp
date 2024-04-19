# Generated by Django 5.0.4 on 2024-04-18 17:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_comment_start_time_alter_comment_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_date',
        ),
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.TextField(max_length=20, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
        ),
    ]
