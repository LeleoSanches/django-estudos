# Generated by Django 4.1.2 on 2022-10-14 17:21

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='alterado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='criado',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 10, 14, 17, 21, 17, 657555, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='publicado',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('rascunho', 'Rascunho'), ('publicado', 'Publicado')], default='rascunho', max_length=10),
        ),
    ]
