# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollsi', '0005_remove_questionn_question_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='question_desc',
            field=models.CharField(default='grk', max_length=180),
            preserve_default=False,
        ),
    ]
