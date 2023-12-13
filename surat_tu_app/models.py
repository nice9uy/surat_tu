from django.db import models

# Create your models here.
def user_folder(instance, filename):
    return f"{instance.username}/surat/{filename}"

def disposisi_kabadan(instance, filename):
    return f"{instance.username}/Disposisi_Kabadan/{filename}"

def disposisi_ses(instance, filename):
    return f"{instance.username}/disposisi_Sesbaranahan/{filename}"

def disposisi_bagum(instance, filename):
    return f"{instance.username}/disposisi_Kabagum/{filename}"

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
    upload_file = models.FileField(upload_to= user_folder, null=False, blank=False)
    class Meta:
        db_table = "DbSurat"

class DisposisiKabadan(models.Model):
    no_surat = models.ForeignKey(DbSurat, on_delete = models.CASCADE)
    catatan = models.CharField(max_length=200, null=True)
    upload_file_disposisi_kabadan = models.FileField(upload_to= disposisi_kabadan, null=True, blank=False)

    class Meta:
        db_table = "DisposisiKabadan"

class DisposisiSes(models.Model):
    no_surat = models.ForeignKey(DbSurat, on_delete = models.CASCADE)
    catatan = models.CharField(max_length=200 , null=True)
    upload_file_disposisi_ses = models.FileField(upload_to= disposisi_ses, null=True, blank=False)

    class Meta:
        db_table = "DisposisiSes"

class DisposisiBagum(models.Model):
    no_surat = models.ForeignKey(DbSurat, on_delete = models.CASCADE)
    catatan = models.CharField(max_length=200 , null=True)
    upload_file_disposisi_bagum = models.FileField(upload_to= disposisi_bagum, null=True, blank=False)

    class Meta:
        db_table = "DisposisiBagum"

class DbKlasifikasi(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    klasifikasi = models.CharField(max_length=30)

    class Meta:
        db_table = "Klasifikasi"