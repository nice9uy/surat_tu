from django.contrib import admin

# Register your models here.
from .models import NotaDinas, SemuaNotaDinas

class ListNotaDinas(admin.ModelAdmin):
    list_display = ('id', 'username','tanggal')

class ListDetailNotaDinas(admin.ModelAdmin):
    list_display = ('id', 'id_semua_nota_dinas','username',
                    'no_urut', 'no_takah', 'kepada',
                    'perihal','keterangan','catatan'
                    )


admin.site.register(NotaDinas,ListNotaDinas)
admin.site.register(SemuaNotaDinas,ListDetailNotaDinas)