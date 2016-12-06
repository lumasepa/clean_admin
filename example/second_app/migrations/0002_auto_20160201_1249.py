# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='big_integer_field',
            field=models.BigIntegerField(help_text=b'An big integer field', null=True),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='binary_field',
            field=models.BinaryField(help_text=b'A binary field', null=True),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='char_field',
            field=models.CharField(help_text=b'write something', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='comma_separated_integer_field',
            field=models.CommaSeparatedIntegerField(help_text=b'A comma sepparated integer field', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='date_field',
            field=models.DateField(help_text=b'A date field', null=True),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='datetime_field',
            field=models.DateTimeField(help_text=b'A datetime field', null=True),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='decimal_field',
            field=models.DecimalField(help_text=b'A decimal field', null=True, max_digits=100, decimal_places=10),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='duration_field',
            field=models.DurationField(help_text=b'A duration field', null=True),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='email_field',
            field=models.EmailField(help_text=b'A email field', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='file_field',
            field=models.FileField(help_text=b'A file field', null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='file_path_field',
            field=models.FilePathField(help_text=b'A file path field', null=True),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='float_field',
            field=models.FloatField(help_text=b'A float field', null=True),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='generic_ip_addr_field',
            field=models.GenericIPAddressField(help_text=b'A generic ip addr field', null=True),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='image_field',
            field=models.ImageField(help_text=b'A image field', null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='int_field',
            field=models.IntegerField(help_text=b'Put a number, magic number', null=True),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='many_to_many_field',
            field=models.ManyToManyField(help_text=b'A many to many field', to='second_app.ManyToManyModel', null=True),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='positive_integer_field',
            field=models.PositiveIntegerField(help_text=b'A positive integer', null=True),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='positive_small_integer_field',
            field=models.PositiveSmallIntegerField(help_text=b'A positive small integer field', null=True),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='slug_field',
            field=models.SlugField(help_text=b'A slug field', null=True),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='small_integer_field',
            field=models.SmallIntegerField(help_text=b'A small integer field', null=True),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='text_field',
            field=models.TextField(help_text=b'Put a large test here', null=True),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='time_field',
            field=models.TimeField(help_text=b'A time field', null=True),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='url_field',
            field=models.URLField(help_text=b'A url field', null=True),
        ),
        migrations.AlterField(
            model_name='allfieldsmodel',
            name='uuid_field',
            field=models.UUIDField(help_text=b'A uuid field', null=True),
        ),
    ]
