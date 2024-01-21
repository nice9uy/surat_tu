from django.contrib import admin

# Register your models here.
from .models import NotaDinas, SemuaNotaDinas

class ListNotaDinas(admin.ModelAdmin):
    list_display = ('id', 'username','tanggal')

class ListDetailNotaDinas(admin.ModelAdmin):
    list_display = ('id', 'id_nota_dinas','username',
                    'tanggal', 'no_takah', 'kepada',
                    'perihal','keterangan','keterangan_tambahan'
                    )


admin.site.register(NotaDinas,ListNotaDinas)
admin.site.register(SemuaNotaDinas,ListDetailNotaDinas)