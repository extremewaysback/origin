# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20151013_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defectdata',
            name='scantime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
