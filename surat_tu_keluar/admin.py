from django.contrib import admin

# Register your models here.
from .models import NotaDinas

class ListNotaDinas(admin.ModelAdmin):
    list_display = ('id', 'username','tanggal','no_urut',
                    'no_takah','kepada','perihal','keterangan',
                    'catatan','bagian','upload_file'
                    )



admin.site.register(NotaDinas,ListNotaDinas)
# admin.site.register(SemuaNotaDinas,ListDetailNotaDinas)