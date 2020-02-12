# Generated by Django 3.0.3 on 2020-02-11 13:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 34, 30, 984090, tzinfo=utc))),
                ('count', models.IntegerField(default=0)),
                ('time_limit', models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 35, 30, 984129, tzinfo=utc))),
                ('status', models.CharField(default='n', max_length=4)),
            ],
        ),
    ]
