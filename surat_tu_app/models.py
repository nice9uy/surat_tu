
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

def save_file_disposisi(instance, filename):
    return f"{instance.username}/Disposisi/{filename}"

def save_file_surat(instance, filename):
    return f"{instance.username}/SuratMasuk/{filename}"
    

class DbSurat(models.Model):
  
    id              = models.AutoField(primary_key=True, unique=True)
    username        = models.CharField(max_length=30)
    jenis_surat     = models.CharField(max_length=30 , null=True , blank=True)
    klasifikasi     = models.CharField(max_length=30 , null=True , blank=True)
    tgl_agenda      = models.DateField()
    id_jenis_surat  = models.CharField(max_length=1)
    no_agenda       = models.CharField(max_length=30 , unique=True)
    tgl_surat       = models.DateField(null=True ,  blank=True)
    no_surat        = models.CharField(max_length=30 )
    surat_dari      = models.CharField(max_length=110)
    derajat_surat   = models.CharField(max_length=30 , null = True, blank=True)
    perihal         = models.CharField(max_length=200)
    upload_file     = models.FileField(upload_to= save_file_surat, null=False, blank=False , validators=[FileExtensionValidator(allowed_extensions=["pdf"])] )

    def __str__(self):
        return self.no_surat
    class Meta:
        db_table = "DbSurat"

class DisposisiDb(models.Model):    
    id                      = models.AutoField(primary_key=True, unique=True)
    username                = models.CharField(max_length=30)
    disposisi               = models.CharField(max_length = 30)
    tgl_disposisi           = models.DateField()
    tgl_disposisi_kembali   = models.DateField(null = True, blank=True)
    no_surat                = models.ForeignKey(DbSurat, on_delete = models.CASCADE )
    no_agenda               = models.CharField(max_length = 30, null=True)
    catatan                 = models.CharField(max_length = 200)
    upload_file_disposisi   = models.FileField(upload_to=save_file_disposisi, null = True, blank=True , validators=[FileExtensionValidator(allowed_extensions=["pdf"])] )


    # def __str__(self):
    #     return self.no_surat

    class Meta:
        db_table = "DisposisiDb"

class DbKlasifikasi(models.Model):
    id          = models.AutoField(primary_key=True, unique=True)
    klasifikasi = models.CharField(max_length=30)

    class Meta:
        db_table = "Klasifikasi"

class DbJenisSurat(models.Model):
    id           = models.AutoField(primary_key=True, unique=True)
    jenis_surat  = models.CharField(max_length=30)
    inisial_nama = models.CharField(max_length=30)

    class Meta:
        db_table = "JenisSurat"

class DbDerajatSurat(models.Model):
    id            = models.AutoField(primary_key=True, unique=True)
    dejarat_surat = models.CharField(max_length=30)

    class Meta:
        db_table = "DbDerajatSurat"

class TempNoAgenda(models.Model):
    username    = models.CharField(max_length=30)
    no_agenda   = models.CharField(max_length=30)
    jenis_surat = models.CharField(max_length=30)
    tgl_agenda  = models.DateField()

    class Meta:
        db_table = "TempNoAgenda"