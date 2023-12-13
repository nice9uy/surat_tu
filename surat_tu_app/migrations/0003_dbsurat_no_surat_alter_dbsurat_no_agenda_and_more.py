# Generated by Django 5.0 on 2023-12-13 02:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surat_tu_app', '0002_remove_dbsurat_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbsurat',
            name='no_surat',
            field=models.TextField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dbsurat',
            name='no_agenda',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='dbsurat',
            name='surat_dari',
            field=models.CharField(max_length=110),
        ),
    ]
