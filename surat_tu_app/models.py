from django.db import models

# Create your models here.
def user_folder(instance, filename):
    return f"{instance.username}/surat/{filename}"

class DbSurat(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    group = models.CharField(max_length=30)
    klasifikasi = models.CharField(max_length=30)
    tgl_agenda = models.DateField()
    no_agenda = models.TextField(max_length=200)
    tgl_surat = models.DateField()
    surat_dari = models.CharField(max_length=200)
    perihal = models.CharField(max_length=200)
    upload_file = models.FileField(upload_to= user_folder, null=False, blank=False)
    class Meta:
        db_table = "DbSurat"

class Klasifikasi(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    klasifikasi = models.CharField(max_length=30)

    class Meta:
        db_table = "Klasifikasi"