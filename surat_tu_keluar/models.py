from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

def save_file_disposisi(instance, filename):
    return f"{instance.username}/Disposisi/{filename}"

def save_file_surat(instance, filename):
    return f"{instance.username}/SuratMasuk/{filename}"
    
class NotaDinas(models.Model):
  
    id                     = models.AutoField(primary_key=True, unique=True)
    username               = models.CharField(max_length=30)
    tanggal                = models.DateField()
   
    class Meta:
        db_table = "NotaDinas"
    
class SemuaNotaDinas(models.Model):

    id                     = models.AutoField(primary_key=True, unique=True)
    id_nota_dinas          = models.ForeignKey(NotaDinas, on_delete = models.CASCADE )
    username               = models.CharField(max_length=30)
    tanggal                = models.DateField()
    no_takah               = models.CharField(max_length=30)
    kepada                 = models.CharField(max_length=30)
    perihal                = models.CharField(max_length=200)
    keterangan             = models.CharField(max_length=200)
    keterangan_tambahan    = models.CharField(max_length=200)

    class Meta:
        db_table = "SemuaNotaDinas"
