# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20160112_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 1, 12, 14, 37, 19, 905583), verbose_name='date of birth(YYYY-MM-DD)', blank=True),
        ),
    ]
