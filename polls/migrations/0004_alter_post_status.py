# Generated by Django 4.1.2 on 2022-10-14 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_post_alterado_post_criado_post_publicado_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('rascunho', 'Rascunho'), ('publicado', 'Publicado'), ('zoado', 'Zoado'), ('fornicado', 'Fornicado')], default='rascunho', max_length=10),
        ),
    ]