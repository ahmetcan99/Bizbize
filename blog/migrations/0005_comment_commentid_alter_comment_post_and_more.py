# Generated by Django 4.2.4 on 2024-05-21 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_commentreply'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commentID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
        migrations.DeleteModel(
            name='CommentReply',
        ),
    ]
