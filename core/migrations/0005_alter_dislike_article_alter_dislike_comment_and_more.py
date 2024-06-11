# Generated by Django 5.0.5 on 2024-05-24 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_dislike_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dislike',
            name='article',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dislikes', to='core.article'),
        ),
        migrations.AlterField(
            model_name='dislike',
            name='comment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dislikes', to='core.comment'),
        ),
        migrations.AlterField(
            model_name='like',
            name='article',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='core.article'),
        ),
        migrations.AlterField(
            model_name='like',
            name='comment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='core.comment'),
        ),
    ]
