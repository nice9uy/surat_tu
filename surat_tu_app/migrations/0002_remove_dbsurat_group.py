# Generated by Django 5.0 on 2023-12-13 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surat_tu_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dbsurat',
            name='group',
        ),
    ]
