from django.contrib import admin

# Register your models here.
from .models import DbSurat
from .models import DbKlasifikasi

class ListDbSurat(admin.ModelAdmin):
    list_display = ('id', 'username','klasifikasi', 'tgl_agenda',
                    'no_agenda','tgl_surat','surat_dari','perihal',
                    'upload_file'
                    )
class ListKlasifikasi(admin.ModelAdmin):
    list_display = ('id','klasifikasi')

admin.site.register(DbSurat,ListDbSurat)
admin.site.register(DbKlasifikasi, ListKlasifikasi)
