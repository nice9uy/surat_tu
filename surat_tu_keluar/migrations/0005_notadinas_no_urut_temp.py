# Generated by Django 5.0 on 2024-03-26 00:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surat_tu_keluar', '0004_biasa'),
    ]

    operations = [
        migrations.AddField(
            model_name='notadinas',
            name='no_urut_temp',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
