# Generated by Django 5.0 on 2024-01-27 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surat_tu_keluar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notadinas',
            old_name='catatan',
            new_name='bon_oleh',
        ),
    ]
