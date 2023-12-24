from django.db import models


class DbSurat(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    klasifikasi = models.CharField(max_length=30)
    tgl_agenda = models.DateField()
    no_agenda = models.CharField(max_length=30)
    tgl_surat = models.DateField()
    no_surat = models.CharField(max_length=30)
    surat_dari = models.CharField(max_length=110)
    perihal = models.CharField(max_length=200)
    upload_file = models.FileField(upload_to= "Surat", null=False, blank=False)

    def __str__(self):
        return self.no_surat
    class Meta:
        db_table = "DbSurat"

class DisposisiDb(models.Model):
    # DbSurat = models.ForeignKey( DbSurat ,on_delete = models.CASCADE )
    # id = models.AutoField(primary_key=True, unique=True)
    disposisi =  models.CharField(max_length = 30)
    no_surat =  models.ForeignKey(DbSurat, on_delete = models.CASCADE)
    no_agenda = models.CharField(max_length = 30, null=True)
    # catatan = models.CharField(max_length = 200)
    upload_file_disposisi = models.FileField(upload_to="Disposisi", null=False, blank=False)


    def __str__(self):
        return self.no_surat

    class Meta:
        db_table = "DisposisiDb"

class DbKlasifikasi(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    klasifikasi = models.CharField(max_length=30)

    class Meta:
        db_table = "Klasifikasi"