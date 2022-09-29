# Generated by Django 3.2.7 on 2022-09-29 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi', '0016_team_offset_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='ltst_rating',
            field=models.FloatField(default=1000.0, verbose_name='最新レーティング'),
        ),
        migrations.AlterField(
            model_name='team',
            name='offset_term',
            field=models.IntegerField(blank=None, default=0, help_text='レーティングがぐんぐん上昇する「ボーナスタイム」の継続期間（試合数）を選択します。<br>この値を変更するとレーティングの再計算が必要になります。', null=None, verbose_name='ボーナスタイム'),
        ),
    ]
