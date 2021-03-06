# Generated by Django 3.0.2 on 2020-01-18 14:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('high_score', models.BigIntegerField(default=0)),
                ('username', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 1, 18, 14, 58, 24, 697386, tzinfo=utc), verbose_name='Date published')),
            ],
        ),
    ]
