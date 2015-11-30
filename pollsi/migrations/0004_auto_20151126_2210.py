# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollsi', '0003_auto_20151126_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=180)),
                ('question_desc', models.CharField(max_length=180)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='pollsi.Questionn'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
