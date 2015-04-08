# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import fias.fields.uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddrObj',
            fields=[
                ('ifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('ifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('okato', models.BigIntegerField(null=True, blank=True)),
                ('oktmo', models.IntegerField(null=True, blank=True)),
                ('postalcode', models.PositiveIntegerField(null=True, blank=True)),
                ('updatedate', models.DateField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('normdoc', fias.fields.uuid.UUIDField(auto=False, null=True, name=b'normdoc', blank=True)),
                ('aoguid', fias.fields.uuid.UUIDField(primary_key=True, serialize=False, editable=False, blank=True, name=b'aoguid')),
                ('parentguid', fias.fields.uuid.UUIDField(db_index=True, auto=False, null=True, name=b'parentguid', blank=True)),
                ('aoid', fias.fields.uuid.UUIDField(name=b'aoid', editable=False, blank=True, unique=True, db_index=True)),
                ('previd', fias.fields.uuid.UUIDField(auto=False, null=True, name=b'previd', blank=True)),
                ('nextid', fias.fields.uuid.UUIDField(auto=False, null=True, name=b'nextid', blank=True)),
                ('formalname', models.CharField(max_length=120, db_index=True)),
                ('offname', models.CharField(max_length=120, null=True, blank=True)),
                ('shortname', models.CharField(max_length=10, db_index=True)),
                ('aolevel', models.PositiveSmallIntegerField(db_index=True)),
                ('regioncode', models.CharField(max_length=2)),
                ('autocode', models.CharField(max_length=1)),
                ('areacode', models.CharField(max_length=3)),
                ('citycode', models.CharField(max_length=3)),
                ('ctarcode', models.CharField(max_length=3)),
                ('placecode', models.CharField(max_length=3)),
                ('streetcode', models.CharField(max_length=4)),
                ('extrcode', models.CharField(max_length=4)),
                ('sextcode', models.CharField(max_length=3)),
                ('code', models.CharField(max_length=17, null=True, blank=True)),
                ('plaincode', models.CharField(max_length=15, null=True, blank=True)),
                ('actstatus', models.BooleanField()),
                ('centstatus', models.PositiveSmallIntegerField()),
                ('operstatus', models.PositiveSmallIntegerField()),
                ('currstatus', models.PositiveSmallIntegerField()),
                ('livestatus', models.BooleanField()),
            ],
            options={
                'ordering': ['aolevel', 'formalname'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AddrObjIndex',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aoguid', fias.fields.uuid.UUIDField(editable=False, name=b'aoguid', blank=True)),
                ('aolevel', models.PositiveSmallIntegerField()),
                ('scname', models.TextField()),
                ('fullname', models.TextField()),
                ('item_weight', models.PositiveSmallIntegerField(default=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('ifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('ifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('okato', models.BigIntegerField(null=True, blank=True)),
                ('oktmo', models.IntegerField(null=True, blank=True)),
                ('postalcode', models.PositiveIntegerField(null=True, blank=True)),
                ('updatedate', models.DateField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('normdoc', fias.fields.uuid.UUIDField(auto=False, null=True, name=b'normdoc', blank=True)),
                ('housenum', models.CharField(max_length=20, null=True, blank=True)),
                ('eststatus', models.BooleanField()),
                ('buildnum', models.CharField(max_length=10, null=True, blank=True)),
                ('strucnum', models.CharField(max_length=10, null=True, blank=True)),
                ('strstatus', models.PositiveSmallIntegerField()),
                ('houseguid', fias.fields.uuid.UUIDField(primary_key=True, serialize=False, editable=False, blank=True, name=b'houseguid')),
                ('houseid', fias.fields.uuid.UUIDField(editable=False, name=b'houseid', blank=True)),
                ('statstatus', models.PositiveSmallIntegerField()),
                ('counter', models.IntegerField()),
                ('aoguid', models.ForeignKey(to='fias.AddrObj')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HouseInt',
            fields=[
                ('ifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('ifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('okato', models.BigIntegerField(null=True, blank=True)),
                ('oktmo', models.IntegerField(null=True, blank=True)),
                ('postalcode', models.PositiveIntegerField(null=True, blank=True)),
                ('updatedate', models.DateField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('normdoc', fias.fields.uuid.UUIDField(auto=False, null=True, name=b'normdoc', blank=True)),
                ('houseintid', fias.fields.uuid.UUIDField(editable=False, name=b'houseintid', blank=True)),
                ('intguid', fias.fields.uuid.UUIDField(primary_key=True, serialize=False, editable=False, blank=True, name=b'intguid')),
                ('intstart', models.PositiveIntegerField()),
                ('intend', models.PositiveIntegerField()),
                ('intstatus', models.PositiveIntegerField()),
                ('counter', models.PositiveIntegerField()),
                ('aoguid', models.ForeignKey(to='fias.AddrObj')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LandMark',
            fields=[
                ('ifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('ifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('okato', models.BigIntegerField(null=True, blank=True)),
                ('oktmo', models.IntegerField(null=True, blank=True)),
                ('postalcode', models.PositiveIntegerField(null=True, blank=True)),
                ('updatedate', models.DateField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('normdoc', fias.fields.uuid.UUIDField(auto=False, null=True, name=b'normdoc', blank=True)),
                ('landid', fias.fields.uuid.UUIDField(editable=False, name=b'landid', blank=True)),
                ('landguid', fias.fields.uuid.UUIDField(primary_key=True, serialize=False, editable=False, blank=True, name=b'landguid')),
                ('location', models.TextField()),
                ('aoguid', models.ForeignKey(to='fias.AddrObj')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NormDoc',
            fields=[
                ('normdocid', fias.fields.uuid.UUIDField(primary_key=True, serialize=False, editable=False, blank=True, name=b'normdocid')),
                ('docname', models.TextField(blank=True)),
                ('docdate', models.DateField(null=True, blank=True)),
                ('docnum', models.CharField(max_length=20, null=True, blank=True)),
                ('doctype', models.IntegerField()),
                ('docimgid', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocrBase',
            fields=[
                ('level', models.PositiveSmallIntegerField(verbose_name='level')),
                ('scname', models.CharField(default=' ', max_length=10)),
                ('socrname', models.CharField(default=' ', max_length=50)),
                ('kod_t_st', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('item_weight', models.PositiveSmallIntegerField(default=64)),
            ],
            options={
                'ordering': ['level', 'scname'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('table', models.CharField(max_length=15, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('ver', models.IntegerField(serialize=False, primary_key=True)),
                ('date', models.DateField(db_index=True, null=True, blank=True)),
                ('dumpdate', models.DateField(db_index=True)),
                ('complete_xml_url', models.CharField(max_length=255)),
                ('delta_xml_url', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='status',
            name='ver',
            field=models.ForeignKey(to='fias.Version'),
            preserve_default=True,
        ),
        migrations.AlterIndexTogether(
            name='socrbase',
            index_together=set([('level', 'scname')]),
        ),
        migrations.AlterIndexTogether(
            name='addrobj',
            index_together=set([('aolevel', 'shortname'), ('shortname', 'formalname')]),
        ),
    ]
