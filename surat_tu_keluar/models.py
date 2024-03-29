from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

def save_file_nota_dinas(instance, filename):
    return f"Surat_Keluar/{instance.username}/NotaDinas/{filename}"

def save_file_biasa(instance, filename):
    return f"Surat_Keluar/{instance.username}/Biasa/{filename}"


class NotaDinas(models.Model):

    id                     = models.AutoField(primary_key=True, unique=True)
    username               = models.CharField(max_length=30)
    tanggal                = models.DateField()
    no_urut                = models.CharField(max_length=50)
    no_urut_temp           = models.CharField(max_length=30)
    no_takah               = models.CharField(max_length=30, null=True ,  blank=True)
    kepada                 = models.CharField(max_length=30, null=True ,  blank=True)
    perihal                = models.CharField(max_length=200, null=True ,  blank=True)
    keterangan             = models.CharField(max_length=200, null=True ,  blank=True)
    bagian                 = models.CharField(max_length=10, null=True ,  blank=True)
    catatan               = models.CharField(max_length=200, null=True ,  blank=True)
    upload_file            = models.FileField(upload_to = save_file_nota_dinas, null = True, blank=True , validators=[FileExtensionValidator(allowed_extensions=["pdf"])] )

    class Meta:
        db_table = "NotaDinas"

class Biasa(models.Model):

    id                     = models.AutoField(primary_key=True, unique=True)
    username               = models.CharField(max_length=30)
    tanggal                = models.DateField()
    no_urut                = models.CharField(max_length=50)
    no_urut_temp           = models.CharField(max_length=30)
    no_takah               = models.CharField(max_length=30, null=True ,  blank=True)
    kepada                 = models.CharField(max_length=30, null=True ,  blank=True)
    perihal                = models.CharField(max_length=200, null=True ,  blank=True)
    keterangan             = models.CharField(max_length=200, null=True ,  blank=True)
    bagian                 = models.CharField(max_length=10, null=True ,  blank=True)
    catatan               = models.CharField(max_length=200, null=True ,  blank=True)
    upload_file            = models.FileField(upload_to = save_file_biasa, null = True, blank=True , validators=[FileExtensionValidator(allowed_extensions=["pdf"])] )

    class Meta:
        db_table = "Biasa"

