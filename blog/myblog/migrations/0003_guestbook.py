# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_remove_article_content_html'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('created', models.DateTimeField()),
            ],
        ),
    ]
