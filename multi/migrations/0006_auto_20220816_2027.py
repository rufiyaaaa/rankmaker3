# Generated by Django 3.2.7 on 2022-08-16 11:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('multi', '0005_alter_team_one_on_one'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 16, 11, 27, 1, 608304, tzinfo=utc), verbose_name='試合日時'),
        ),
        migrations.AlterField(
            model_name='game',
            name='last_modify',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 16, 11, 27, 1, 620674, tzinfo=utc), verbose_name='最終更新日'),
        ),
        migrations.AlterField(
            model_name='team',
            name='description',
            field=models.TextField(blank=True, help_text='チームの説明を入力します。ランキングをシェアした際に表示されます。', max_length=500, null=True, verbose_name='説明'),
        ),
    ]
