# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='defectdata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.CharField(max_length=30)),
                ('layer', models.CharField(max_length=30, choices=[(b'ACT_ADI', b'ACT_ADI'), (b'ACT_AEI', b'ACT_AEI'), (b'PLY1_ADI', b'PLY1_ADI'), (b'PLY1_AEI', b'PLY1_AEI'), (b'MET1_ADI', b'MET1_ADI'), (b'MET1_AEI', b'MET1_AEI')])),
                ('lot', models.CharField(max_length=10)),
                ('wafer', models.CharField(max_length=10)),
                ('scantime', models.DateField()),
                ('defectcount', models.IntegerField()),
                ('remarks', models.TextField()),
            ],
        ),
    ]
