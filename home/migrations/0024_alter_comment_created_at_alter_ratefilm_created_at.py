# Generated by Django 5.0.4 on 2024-04-15 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_comment_created_at_alter_ratefilm_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 15, 19, 39, 36, 918847, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='ratefilm',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 15, 19, 39, 36, 919847, tzinfo=datetime.timezone.utc)),
        ),
    ]