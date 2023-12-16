from django.contrib import admin

# Register your models here.
from .models import DbSurat
from .models import DbKlasifikasi
from .models import DisposisiKabadan
from .models import DisposisiSes
from .models import DisposisiBagum

class ListDbSurat(admin.ModelAdmin):
    list_display = ('id', 'username','klasifikasi', 'tgl_agenda',
                    'no_agenda','tgl_surat','surat_dari','perihal',
                    'upload_file'
                    )
    
class ListKlasifikasi(admin.ModelAdmin):
    list_display = ('id','klasifikasi')



class ListDisposisiKabadan(admin.ModelAdmin):
    list_display = ('no_surat','tgl_agenda',
                    'no_agenda', 'catatan',
                    'upload_file_disposisi_kabadan',
                    )

class ListDisposisiSes(admin.ModelAdmin):
       list_display = ('no_surat','tgl_agenda',
                    'no_agenda', 'catatan',
                    'upload_file_disposisi_ses',
                    )


class ListDisposisiBagum(admin.ModelAdmin):
     list_display = ('no_surat','tgl_agenda',
                    'no_agenda', 'catatan',
                    'upload_file_disposisi_bagum',
                    )


admin.site.register(DbSurat,ListDbSurat)
admin.site.register(DbKlasifikasi, ListKlasifikasi)
admin.site.register(DisposisiKabadan, ListDisposisiKabadan)
admin.site.register(DisposisiSes, ListDisposisiSes)
admin.site.register(DisposisiBagum, ListDisposisiBagum)
