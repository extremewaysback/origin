# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20151013_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defectdata',
            name='scantime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
