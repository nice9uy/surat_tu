# Generated by Django 5.0 on 2023-12-13 04:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surat_tu_app', '0004_alter_dbsurat_no_agenda_alter_dbsurat_no_surat'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbsurat',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
