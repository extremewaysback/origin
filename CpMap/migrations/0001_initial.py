# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cpdata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.DecimalField(max_digits=5, decimal_places=2)),
                ('y', models.DecimalField(max_digits=5, decimal_places=2)),
                ('c', models.CharField(max_length=10)),
                ('f', models.FileField(upload_to=b'')),
            ],
        ),
    ]
