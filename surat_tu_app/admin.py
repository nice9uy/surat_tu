from django.contrib import admin

# Register your models here.
from .models import DbSurat
from .models import DbKlasifikasi
from .models import DisposisiDb
from .models import DbJenisSurat
from .models import DbDerajatSurat
from .models import TempNoAgenda


class ListDbSurat(admin.ModelAdmin):
    list_display = ('id', 'username','klasifikasi', 'tgl_agenda',
                    'id_jenis_surat','no_agenda','tgl_surat','no_surat','surat_dari','perihal','derajat_surat',
                    'upload_file'
                    )
    
class ListKlasifikasi(admin.ModelAdmin):
    list_display = ('id','klasifikasi')

class ListDbJenisSurat(admin.ModelAdmin):
    list_display = ('id','jenis_surat','inisial_nama')

class ListDbDerajatSurat(admin.ModelAdmin):
    list_display = ('id','dejarat_surat')

class ListDisposisiDb(admin.ModelAdmin):
    list_display = ( 'no_surat', 'no_surat_id', 'id' , 'username','disposisi','tgl_disposisi', 'no_agenda', 'catatan','upload_file_disposisi',
                    )
    
class ListTempNoAgenda(admin.ModelAdmin):
    list_display = ('username','no_agenda','jenis_surat')


admin.site.site_header = 'Admin ARSIP TU SETBARANAHAN'                    # default: "Django Administration"
admin.site.index_title = 'SEMUA DATABASE ARSIP'   


admin.site.register(DbSurat,ListDbSurat)
admin.site.register(DbKlasifikasi, ListKlasifikasi)
admin.site.register(DisposisiDb , ListDisposisiDb)
admin.site.register(DbJenisSurat , ListDbJenisSurat)
admin.site.register(DbDerajatSurat , ListDbDerajatSurat)
admin.site.register(TempNoAgenda , ListTempNoAgenda)

