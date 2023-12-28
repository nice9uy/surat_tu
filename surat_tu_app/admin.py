from django.contrib import admin

# Register your models here.
from .models import DbSurat
from .models import DbKlasifikasi
from .models import DisposisiDb
from .models import DbJenisSurat


class ListDbSurat(admin.ModelAdmin):
    list_display = ('id', 'username','klasifikasi', 'tgl_agenda',
                    'no_agenda','tgl_surat','no_surat','surat_dari','perihal',
                    'upload_file'
                    )
    
class ListKlasifikasi(admin.ModelAdmin):
    list_display = ('id','klasifikasi')

class ListDbJenisSurat(admin.ModelAdmin):
    list_display = ('id','jenis_surat','inisial_nama')

class ListDisposisiDb(admin.ModelAdmin):
    list_display = ( 'no_surat', 'no_surat_id', 'id' , 'username','disposisi','no_agenda', 'catatan','upload_file_disposisi',
                    )


admin.site.register(DbSurat,ListDbSurat)
admin.site.register(DbKlasifikasi, ListKlasifikasi)
admin.site.register(DisposisiDb , ListDisposisiDb)
admin.site.register(DbJenisSurat , ListDbJenisSurat)

