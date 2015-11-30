# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollsi', '0006_choice_question_desc'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Questionn',
            new_name='Question',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question_desc',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_desc',
            field=models.CharField(default='grk', max_length=170),
            preserve_default=False,
        ),
    ]
