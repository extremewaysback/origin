# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20160112_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 1, 12, 14, 45, 51, 498765), verbose_name='date of birth(YYYY-MM-DD)', blank=True),
        ),
    ]
