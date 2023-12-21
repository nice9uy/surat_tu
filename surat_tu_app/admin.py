from django.contrib import admin

# Register your models here.
from .models import DbSurat
from .models import DbKlasifikasi
from .models import DisposisiDb

class ListDbSurat(admin.ModelAdmin):
    list_display = ('id', 'username','klasifikasi', 'tgl_agenda',
                    'no_agenda','tgl_surat','surat_dari','perihal',
                    'upload_file'
                    )
    
class ListKlasifikasi(admin.ModelAdmin):
    list_display = ('id','klasifikasi')

class ListDisposisiDb(admin.ModelAdmin):
    list_display = ( 'id','disposisi','no_surat','no_agenda','upload_file_disposisi',
                    )


admin.site.register(DbSurat,ListDbSurat)
admin.site.register(DbKlasifikasi, ListKlasifikasi)
admin.site.register(DisposisiDb , ListDisposisiDb)

